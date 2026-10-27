"""Ежедневное повторение английского: страница-чек-лист + сообщение и квизы в Telegram.

  python bot/daily.py --build            собрать страницу дня в docs/day/
  python bot/daily.py --send             отправить сообщение и квизы в Telegram
  python bot/daily.py --build --dry-run --date 2026-11-02   проверить без отправки
"""
import argparse, datetime as dt, html, json, os, random, re, sys, time
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).parent))
from bank import BANK  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
MSK = dt.timezone(dt.timedelta(hours=CFG.get("utc_offset_hours", 3)))
WORDS_PER_DAY = 15


# ---------- данные ----------
def load_topics():
    text = (ROOT / "data" / "konspekt.md").read_text(encoding="utf-8")
    topics, group = {}, None
    for block in re.split(r"^(?=@@group |## )", text, flags=re.M):
        if block.startswith("@@group "):
            group = block[8:].strip()
            continue
        m = re.match(r"## (\d+)\.\s+([^\n]*)\n(.*)", block, flags=re.S)
        if m:
            topics[int(m.group(1))] = dict(num=int(m.group(1)), title=m.group(2).strip(), body=m.group(3).strip(), group=group)
    return topics


def load_words():
    words, cat = [], None
    for line in (ROOT / "data" / "words.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if line.startswith("@"):
            cat = line[3:].strip()
            continue
        en, ru, _ = [p.strip() for p in line.split(" | ")]
        words.append(dict(en=en, ru=ru, cat=cat))
    return words


def rule_part(body):
    """Объяснение темы без блока примеров."""
    return re.split(r"^(?:Примеры|Другие примеры):\s*$", body, flags=re.M)[0].strip()


# ---------- план дня ----------
def plan(date):
    start = dt.date.fromisoformat(CFG["start_date"])
    idx = max(0, (date - start).days)
    topics = load_topics()
    order = sorted(n for n in topics if n in BANK)
    topic = topics[order[idx % len(order)]]
    words = load_words()
    random.Random(CFG.get("seed", 2026)).shuffle(words)
    s = (idx * WORDS_PER_DAY) % len(words)
    day_words = [words[(s + i) % len(words)] for i in range(WORDS_PER_DAY)]
    return dict(idx=idx, n=idx + 1, date=date, topic=topic, words=day_words, all_words=words)


def distractors(word, pool, field, k, rnd):
    same = [w[field] for w in pool if w["cat"] == word["cat"] and w[field] != word[field]]
    other = [w[field] for w in pool if w["cat"] != word["cat"] and w[field] != word[field]]
    rnd.shuffle(same); rnd.shuffle(other)
    out = []
    for x in same + other:
        if x not in out:
            out.append(x)
        if len(out) == k:
            break
    return out


def mcq_word(word, pool, rnd, direction):
    src, dst = ("en", "ru") if direction == "en-ru" else ("ru", "en")
    opts = distractors(word, pool, dst, 3, rnd) + [word[dst]]
    rnd.shuffle(opts)
    if direction == "en-ru":
        q = f"Что значит «{word['en']}»?"
    else:
        q = f"Как по-английски: «{word['ru']}»?"
    return dict(text=q, options=opts, answer=opts.index(word[dst]), explain=f"{word['en']} — {word['ru']}")


# ---------- вопросы для страницы ----------
def page_questions(p):
    t, b = p["topic"], BANK[p["topic"]["num"]]
    rnd = random.Random(p["idx"] * 7919 + 1)
    g = {"Времена": 0, "Привычки": 1, "Пассив": 2, "Условные предложения": 3, "Модальные глаголы": 4}.get(t["group"], 5)
    qs = [dict(sec=f"Грамматика: {t['title']}", g=g)]
    for i, (q, opts, ans, ex) in enumerate(b["mcq"]):
        qs.append(dict(id=f"g{i+1}", type="radio", kind="Выберите один вариант", text=q, options=opts, answer=ans, explain=ex))
    bank, parts = b["gap"]
    qs.append(dict(id="g5", type="gap", kind="Заполните пропуски", bank=bank,
                   parts=[[a, ans, c] for a, ans, c in parts], explain="Сверьтесь с правилом в подсказке выше."))
    mq, mopts, mans, mex = b["multi"]
    qs.append(dict(id="g6", type="multi", kind="Выберите все правильные варианты", text=mq, options=mopts, answer=mans, explain=mex))

    w = p["words"]
    qs.append(dict(sec="Словарь: 15 слов и выражений", g=6))
    qs.append(dict(id="v1", type="match", kind="Сопоставьте выражение и перевод", text="Английский → русский",
                   pairs=[[x["en"], x["ru"]] for x in w[0:5]], explain="Повторите эти слова в словаре конспекта."))
    qs.append(dict(id="v2", type="match", kind="Сопоставьте перевод и выражение", text="Русский → английский",
                   pairs=[[x["ru"], x["en"]] for x in w[5:10]], explain="Повторите эти слова в словаре конспекта."))
    for i, x in enumerate(w[10:15]):
        m = mcq_word(x, p["all_words"], rnd, "en-ru")
        qs.append(dict(id=f"v{i+3}", type="radio", kind="Выберите перевод", **m))
    return qs


def esc_tree(o):
    if isinstance(o, str):
        return html.escape(o, quote=False)
    if isinstance(o, list):
        return [esc_tree(x) for x in o]
    if isinstance(o, dict):
        return {k: (v if k in ("type", "id", "kind", "sec") else esc_tree(v)) for k, v in o.items()}
    return o


def build_page(p):
    t = p["topic"]
    tpl = (ROOT / "bot" / "templates" / "quiz.html").read_text(encoding="utf-8")
    css = (ROOT / "bot" / "templates" / "glass.css").read_text(encoding="utf-8")
    words_line = ", ".join(x["en"] for x in p["words"])
    qs = esc_tree(page_questions(p))
    rep = {
        "TITLE": f"Повторение №{p['n']}",
        "BADGE": f"Повторение №{p['n']}",
        "DATE": p["date"].strftime("%d.%m.%Y"),
        "H1": html.escape(f"{t['title']} + 15 слов"),
        "HERO_P": html.escape(f"Грамматика: тема {t['num']} конспекта. Слова: {words_line}."),
        "RULE_G": "3",
        "RULE": markdown.markdown(rule_part(t["body"]), extensions=["tables"]),
        "QUESTIONS": json.dumps(qs, ensure_ascii=False),
        "KEY": f"review-{p['n']}-state",
        "TOPIC_NUM": str(t["num"]),
    }
    out = tpl.replace("/*GLASS*/", css)
    for k, v in rep.items():
        out = out.replace("{{" + k + "}}", v)
    path = ROOT / "docs" / "day" / f"{p['n']:03d}.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(out, encoding="utf-8")
    return path


# ---------- Telegram ----------
def pages_url():
    if os.environ.get("PAGES_URL"):
        return os.environ["PAGES_URL"].rstrip("/") + "/"
    repo = os.environ.get("GITHUB_REPOSITORY", "owner/repo")
    owner, name = repo.split("/")
    return f"https://{owner.lower()}.github.io/{name}/"


def tg_rule_text(body, limit=1400):
    lines = []
    for line in rule_part(body).splitlines():
        if line.strip().startswith("|"):
            continue
        line = html.escape(line, quote=False)
        line = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line)
        line = re.sub(r"^\s*-\s+", "• ", line)
        lines.append(line)
    txt = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    if len(txt) > limit:
        txt = txt[:limit].rsplit(" ", 1)[0] + "…"
    return txt


def cut(s, n):
    return s if len(s) <= n else s[: n - 1] + "…"


def telegram_payloads(p):
    t, b = p["topic"], BANK[p["topic"]["num"]]
    base = pages_url()
    link = f"{base}day/{p['n']:03d}.html"
    words = "\n".join(f"• {html.escape(x['en'], quote=False)} — {html.escape(x['ru'], quote=False)}" for x in p["words"])
    msg = (f"📚 <b>Повторение №{p['n']}</b> · {p['date'].strftime('%d.%m.%Y')}\n\n"
           f"<b>Тема {t['num']}. {html.escape(t['title'], quote=False)}</b>\n{tg_rule_text(t['body'])}\n\n"
           f"<b>Слова дня</b>\n{words}\n\n"
           f"Ниже 8 коротких квизов. Полный чек-лист — по кнопке 👇")
    out = [("sendMessage", dict(text=msg, parse_mode="HTML", disable_web_page_preview=True,
                                reply_markup=dict(inline_keyboard=[[dict(text="✅ Открыть чек-лист", url=link)],
                                                                  [dict(text="📖 Конспект и словарь", url=base)]])))]
    rnd = random.Random(p["idx"] * 104729 + 3)
    polls = [(f"Грамматика · {q}", opts, ans, ex) for q, opts, ans, ex in b["mcq"]]
    w = p["words"]
    for x in (w[10], w[11]):
        m = mcq_word(x, p["all_words"], rnd, "en-ru")
        polls.append(("Словарь · " + m["text"], m["options"], m["answer"], m["explain"]))
    for x in (w[5], w[6]):
        m = mcq_word(x, p["all_words"], rnd, "ru-en")
        polls.append(("Словарь · " + m["text"], m["options"], m["answer"], m["explain"]))
    for q, opts, ans, ex in polls:
        out.append(("sendPoll", dict(question=cut(q, 300), options=[dict(text=cut(o, 100)) for o in opts],
                                     type="quiz", correct_option_id=ans, is_anonymous=False, explanation=cut(ex, 200))))
    return out


def send(payloads):
    import requests
    token, chat = os.environ.get("TELEGRAM_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        sys.exit("Нет TELEGRAM_TOKEN или TELEGRAM_CHAT_ID (добавьте их в Secrets репозитория).")
    for method, data in payloads:
        data = dict(data, chat_id=chat)
        r = requests.post(f"https://api.telegram.org/bot{token}/{method}", json=data, timeout=30)
        if not r.ok or not r.json().get("ok"):
            sys.exit(f"Telegram {method}: {r.status_code} {r.text}")
        time.sleep(0.6)
    print(f"Отправлено сообщений: {len(payloads)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--send", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="показать, что уйдёт в Telegram, без отправки")
    ap.add_argument("--date", help="YYYY-MM-DD, по умолчанию сегодня по Москве")
    a = ap.parse_args()
    date = dt.date.fromisoformat(a.date) if a.date else dt.datetime.now(MSK).date()
    p = plan(date)
    print(f"День {p['n']} ({date}): тема {p['topic']['num']} «{p['topic']['title']}», слова: {', '.join(x['en'] for x in p['words'])}")
    if a.build:
        print("Страница:", build_page(p).relative_to(ROOT))
    if a.send or a.dry_run:
        pl = telegram_payloads(p)
        if a.dry_run:
            for m, d in pl:
                print(f"\n--- {m} ---\n" + json.dumps(d, ensure_ascii=False, indent=1)[:1500])
        else:
            send(pl)


if __name__ == "__main__":
    main()
