"""Показывает chat_id всех, кто написал боту. Сначала отправьте боту любое сообщение (например /start)."""
import os, sys, requests

token = os.environ.get("TELEGRAM_TOKEN")
if not token:
    sys.exit("Добавьте секрет TELEGRAM_TOKEN.")
r = requests.get(f"https://api.telegram.org/bot{token}/getUpdates", timeout=30).json()
if not r.get("ok"):
    sys.exit(f"Ошибка Telegram: {r}")
seen = {}
for u in r["result"]:
    m = u.get("message") or u.get("my_chat_member") or {}
    c = m.get("chat")
    if c:
        seen[c["id"]] = c.get("username") or c.get("first_name") or c.get("title")
if not seen:
    print("Пока пусто: напишите боту /start в Telegram и запустите этот шаг ещё раз.")
for cid, name in seen.items():
    print(f"TELEGRAM_CHAT_ID = {cid}   ({name})")
