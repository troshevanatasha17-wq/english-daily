# Банк грамматических вопросов по темам конспекта (номер темы = номер в конспекте).
# mcq:   (вопрос, [варианты], индекс правильного, пояснение ≤200 символов) — идут и в квизы Telegram
# gap:   (bank, [(до, [правильные ответы], после), ...])
# multi: (вопрос, [варианты], [индексы правильных], пояснение)

BANK = {
1: dict(
    mcq=[
        ("Yesterday she ___ a new jacket.", ["buy", "bought", "has bought", "was buying"], 1, "Конкретное событие в прошлом (yesterday) → Past Simple."),
        ("___ you go to the concert last week?", ["Did", "Were", "Have", "Do"], 0, "Вопрос в Past Simple: Did + subject + базовая форма."),
        ("My friends ___ me to go to the opera.", ["persuade", "persuaded", "persuading", "have persuade"], 1, "Событие в рассказе о прошлом → V2: persuaded."),
        ("I ___ interested in opera at first.", ["didn't", "wasn't", "haven't", "weren't"], 1, "Для to be в прошедшем — was / were: I wasn't."),
    ],
    gap=(["went", "didn't like", "was"], [
        ("I ", ["went"], " to the circus once."),
        ("She ", ["didn't like", "did not like"], " the new album."),
        ("It ", ["was"], " a clear night and you could see the stars."),
    ]),
    multi=("Какие предложения в Past Simple построены правильно?",
           ["I traveled through Italy last summer.", "Did you went to the party?", "She didn't like the film.", "We was at home yesterday.", "He bought a drum and taught himself to play."],
           [0, 2, 4], "После did — базовая форма: Did you go. С we — were."),
),
2: dict(
    mcq=[
        ("I ___ TV at 8 p.m. yesterday.", ["watched", "was watching", "have watched", "am watching"], 1, "Действие в процессе в конкретный момент прошлого → was/were + V-ing."),
        ("I was sleeping when the phone ___.", ["was ringing", "rang", "has rung", "rings"], 1, "Длительное действие прервано другим → Past Simple."),
        ("It was raining while we ___.", ["walked", "were walking", "have walked", "walk"], 1, "Два действия одновременно → оба в Past Continuous."),
        ("They ___ live when the lights went out.", ["performed", "were performing", "have performed", "perform"], 1, "Фон, который прервали: Past Continuous + Past Simple."),
    ],
    gap=(["were watching", "was riding", "were dancing"], [
        ("While we ", ["were watching"], " the film, we heard a song from my childhood."),
        ("I ", ["was riding"], " the subway when I realised I was late."),
        ("The people around ", ["were dancing"], " all night."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["She was reading while he was cooking.", "I was walking along the beach when I realised that…", "We were watch TV.", "When the phone rang, I was sleeping.", "He were working at 9 p.m."],
           [0, 1, 3], "Форма: was / were + V-ing. He was working."),
),
3: dict(
    mcq=[
        ("When we arrived, the train ___.", ["already left", "had already left", "has already left", "was already leaving"], 1, "Действие раньше другого действия в прошлом → had + V3."),
        ("I realised I ___ my phone in the car.", ["left", "had left", "have left", "was leaving"], 1, "Сначала оставила, потом поняла → Past Perfect."),
        ("I fainted because I ___ too much.", ["drank", "had drunk", "have drunk", "was drink"], 1, "Причина случилась раньше → had drunk."),
        ("Before that I ___ a cockroach in a flat.", ["never saw", "had never seen", "have never seen", "never had saw"], 1, "Опыт до момента в прошлом → had never seen."),
    ],
    gap=(["had lost", "had played", "had forgotten"], [
        ("She realised it was the ring she ", ["had lost"], " last year."),
        ("The band ", ["had played", "had already played"], " their biggest hit when we arrived."),
        ("It turned out I ", ["had forgotten"], " to bring the right card."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["When I got home, I realised I had left my keys at work.", "She had lost the ring a year before she found it.", "I had see this film before.", "When we arrived, the party had already started.", "He has finished before I came."],
           [0, 1, 3], "Форма: had + V3 (had seen). Для действия раньше другого в прошлом — had, не has."),
),
4: dict(
    mcq=[
        ("Have you done your homework ___?", ["already", "yet", "ever", "since"], 1, "yet — в вопросах и отрицаниях."),
        ("They ___ to Australia.", ["have never been", "never was", "have never went", "has never been"], 0, "Жизненный опыт → have + never + V3 (been)."),
        ("She ___ in this city for five years.", ["lives", "has lived", "lived for", "is living since"], 1, "Началось в прошлом и продолжается → Present Perfect."),
        ("He ___ his arm, so he can't play today.", ["broke yesterday", "has broken", "have broken", "breaks"], 1, "Результат в настоящем → has + V3."),
    ],
    gap=(["hasn't given", "have just finished", "have never been"], [
        ("Yulia ", ["hasn't given", "has not given"], " birth yet."),
        ("I ", ["have just finished", "have finished"], " my work — let's go!"),
        ("I ", ["have never been"], " to a concert like that before."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["Have you ever been to Fethiye?", "I haven't been to the gym yet.", "I have visited Paris last year.", "We haven't bought a present yet.", "Did you ever been to Italy?"],
           [0, 1, 3], "С точным временем (last year) нужен Past Simple, не Present Perfect."),
),
5: dict(
    mcq=[
        ("I ___ to them for 5 years.", ["listen", "have been listening", "am listening", "was listening"], 1, "Длится до сих пор + for → have been + V-ing."),
        ("They ___ this hotel for 30 years.", ["run", "have been running", "are running", "ran since"], 1, "Present Perfect Continuous: have/has been + V-ing."),
        ("How long ___ English?", ["are you learning", "have you been learning", "do you learn", "did you learning"], 1, "Как долго длится → Present Perfect Continuous."),
        ("Форма Present Perfect Continuous:", ["have/has + V3", "have/has been + V-ing", "had been + V-ing", "was/were + V-ing"], 1, "have / has been + V-ing."),
    ],
    gap=(["have been working", "has been raining", "have been waiting"], [
        ("We ", ["have been working"], " together for a year."),
        ("It ", ["has been raining"], " since morning."),
        ("I ", ["have been waiting"], " for a developer for a month."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["I've been listening to them for 5 years.", "She has been working here since 2020.", "They have been run this hotel for years.", "We've been working together for a year.", "He been waiting for an hour."],
           [0, 1, 3], "Нужны все части: have/has + been + V-ing."),
),
6: dict(
    mcq=[
        ("I ___ call you, but I was too busy.", ["am going to", "was going to", "will", "would going to"], 1, "Запланированное в прошлом, но не случилось → was going to."),
        ("I thought I ___ cry.", ["will", "would", "am going to", "was"], 1, "Будущее в прошлом: think → thought, will → would."),
        ("Sorry — I crashed the car! I ___!", ["didn't mean to", "wasn't mean to", "don't mean", "didn't intended"], 0, "didn't mean to — сделал случайно."),
        ("They ___ to become global superstars.", ["weren't expecting", "didn't expected", "aren't expecting", "wasn't expect"], 0, "was/were expecting to — прошлые ожидания."),
    ],
    gap=(["planned to", "was hoping to", "intended to"], [
        ("I ", ["planned to"], " visit last week, but I couldn't in the end."),
        ("I ", ["was hoping to"], " meet your father, but he wasn't there."),
        ("He bought the ring because he ", ["intended to"], " ask her to marry him."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["I was going to call you, but I was too busy.", "I meant to introduce you to Xavier.", "I thought I will cry.", "We were planning to take you to the café.", "She didn't meant to do it."],
           [0, 1, 3], "После thought — would, не will. После didn't — mean, не meant."),
),
7: dict(
    mcq=[
        ("I ___ smoke, but I gave up.", ["use to", "used to", "would", "was used to"], 1, "Привычка в прошлом, которой больше нет → used to."),
        ("___ you use to play football?", ["Did", "Were", "Used", "Do"], 0, "Вопрос: Did you use to…?"),
        ("When I was a child, I ___ afraid of dogs.", ["would be", "used to be", "was used to be", "would to be"], 1, "would нельзя со stative verbs (be) → used to be."),
        ("Every morning my grandmother ___ make pancakes.", ["would", "used", "was", "use"], 0, "would — повторяющиеся действия в прошлом."),
    ],
    gap=(["used to", "didn't use to", "would"], [
        ("I ", ["used to"], " have long hair, but now it's short."),
        ("She ", ["didn't use to", "did not use to"], " like coffee, but now she drinks three cups a day."),
        ("After school we ", ["would", "used to"], " meet in the park and play football."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["I used to work in a small café.", "I would be fat when I was young.", "Did you use to smoke?", "We would go to bed at 3 am.", "Did you used to live here?"],
           [0, 2, 3], "would не используют с be. После did — use, не used."),
),
8: dict(
    mcq=[
        ("I'm used to ___ up early.", ["get", "getting", "got", "to get"], 1, "После be/get used to — существительное или V-ing."),
        ("Don't worry, you'll ___ it!", ["get used to", "be use", "used to", "using to"], 0, "get used to — процесс привыкания."),
        ("I've lived here for 10 years, so I ___ the noise.", ["am used to", "used to", "get use to", "am use to"], 0, "be used to — уже привыкла, это нормально."),
        ("Что означает процесс «привыкать»?", ["be used to", "get used to", "used to", "would"], 1, "get used to — процесс, be used to — состояние."),
    ],
    gap=(["getting used to", "used to", "get used to"], [
        ("I'm ", ["getting used to"], " waking up early."),
        ("We are not ", ["used to"], " the climate."),
        ("I'd never ", ["get used to"], " working at night."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["I'm used to speaking a lot in meetings.", "I'm used to speak English.", "It was hard to get used to waking up early.", "She's getting used to her new job.", "We are used to work late."],
           [0, 2, 3], "После be/get used to — V-ing: used to speaking, used to working."),
),
9: dict(
    mcq=[
        ("You're always ___ your phone!", ["lose", "losing", "lost", "to lose"], 1, "always + Continuous — раздражающая привычка."),
        ("Our car was continually ___ down.", ["break", "breaking", "broke", "broken"], 1, "Past Continuous + continually — постоянно ломалась."),
        ("It drives me crazy ___ people use their phone next to me.", ["that", "when", "what", "if not"], 1, "Фразу раздражения продолжают when + clause."),
        ("О прошлом: It gets on my nerves →", ["It got on my nerves", "It was get on my nerves", "It getting on my nerves", "It gots on my nerves"], 0, "О прошлом — те же фразы в Past Simple."),
    ],
    gap=(["forever complaining", "constantly buzzing", "can't stand"], [
        ("My dad's ", ["forever complaining"], " about noise."),
        ("This light drives me mad. It's ", ["constantly buzzing"], "."),
        ("I ", ["can't stand", "cannot stand"], " people shortening my name."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["You're always interrupting me!", "He's constantly losing his keys.", "She always is complaining.", "It doesn't bother me at all.", "It drive me crazy."],
           [0, 1, 3], "Порядок: be + always + V-ing (She's always complaining). It drives."),
),
10: dict(
    mcq=[
        ("The app ___ over a million times.", ["has downloaded", "has been downloaded", "was download", "is downloading"], 1, "Present Perfect passive: has been + V3."),
        ("We ___ followed!", ["are being", "are been", "being", "were be"], 0, "Present Continuous passive: am/is/are being + V3."),
        ("The play ___ by Shakespeare in 1609.", ["wrote", "was written", "has written", "is writing"], 1, "Past Simple passive + by (исполнитель важен)."),
        ("It should ___ done.", ["be", "been", "being", "is"], 0, "С модальными: modal + be + V3."),
    ],
    gap=(["was arrested", "will be announced", "hasn't been sent"], [
        ("Jude ", ["was arrested"], " at the festival last week."),
        ("The winner ", ["will be announced"], " tomorrow."),
        ("The report has been signed, but it ", ["hasn't been sent", "has not been sent"], " yet."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["My train has just been cancelled.", "I got stopped by the police last night.", "The museum was build in 1980.", "The finale was spoiled on social media.", "More series are being make."],
           [0, 1, 3], "В пассиве всегда V3: was built, are being made."),
),
11: dict(
    mcq=[
        ("If it's 0 degrees, water ___.", ["freezes", "will freeze", "froze", "would freeze"], 0, "Zero Conditional — всегда правда: Present + Present."),
        ("If I have time, I ___ you.", ["call", "'ll call", "would call", "called"], 1, "First Conditional: if + Present, will + глагол."),
        ("When I ___ home, I'll call you.", ["will get", "get", "got", "would get"], 1, "После when / if — Present Simple, не will."),
        ("___ you don't like it?", ["What if", "If what", "When", "Unless"], 0, "What if + Present Simple — «а что если…?»"),
    ],
    gap=(["don't sleep", "will affect", "don't have"], [
        ("If I ", ["don't sleep", "do not sleep"], " well, I usually feel terrible."),
        ("If I have one lesson instead of two, it ", ["will affect", "'ll affect"], " my level."),
        ("If I ", ["don't have", "do not have"], " money, I'll borrow it from you."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["If I don't sleep well, I feel terrible.", "If I will have time, I'll call you.", "When I become a millionaire, I won't call you.", "If it rains, we'll stay at home.", "If water will boil, it turns to steam."],
           [0, 2, 3], "В части с if не ставим will: If I have time…"),
),
12: dict(
    mcq=[
        ("Take a jumper with you ___ it gets cold.", ["unless", "even if", "in case", "in case of"], 2, "in case + clause — на случай, если."),
        ("I'm going to the party ___ it rains. Nothing will stop me!", ["in case", "even if", "unless", "in case of"], 1, "even if — даже если."),
        ("She won't pass the exam ___ she studies hard.", ["unless", "in case", "even if", "in case of"], 0, "unless = if not."),
        ("Call this number ___ emergency.", ["in case", "in case of", "unless", "even if"], 1, "in case of + noun — в случае чего-то."),
    ],
    gap=(["unless", "even if", "in case"], [
        ("You won't learn anything ", ["unless"], " you pay attention in class."),
        ("Alex will help me ", ["even if"], " he doesn't want to."),
        ("Take an umbrella ", ["in case"], " it rains."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["Unless you save money, you won't be able to travel.", "In case of it rains, we'll stay at home.", "I'm going to take a first aid kit in case of accidents.", "Unless you don't invite her, Akira won't come.", "I'll travel alone even if I feel lonelier that way."],
           [0, 2, 4], "in case of — только перед существительным. После unless не нужно второе отрицание."),
),
13: dict(
    mcq=[
        ("If I ___ a dragon, I would burn some villages.", ["am", "were", "will be", "would be"], 1, "Second Conditional: if + Past Simple (were), would + infinitive."),
        ("If I saw a book in a shop, I ___ it.", ["steal", "would steal", "will steal", "stole"], 1, "Воображаемая ситуация → would + infinitive."),
        ("If you ___ be any fictional character, who would you be?", ["can", "could", "will", "would"], 1, "В условии — Past Simple: could."),
        ("It ___ be nice if we had more time.", ["will", "would", "is", "was"], 1, "It would be nice if… — гипотетическое."),
    ],
    gap=(["needed", "could", "would"], [
        ("I'd try to download it for free if I really ", ["needed"], " to read it."),
        ("If it was in the library, you ", ["could"], " get it for free."),
        ("What ", ["would"], " you do if you could solve any mystery?"),
    ]),
    multi=("Какие предложения построены правильно?",
           ["If I were in a bookshop, I wouldn't steal a book.", "If I would have money, I'd travel.", "Wouldn't it be scary if…?", "If I had a car, I'd drive to work.", "If I am rich, I would buy a house."],
           [0, 2, 3], "В условии — Past Simple (had, were), would — только в результате."),
),
14: dict(
    mcq=[
        ("If I had prepared, I ___ better.", ["would answer", "would have answered", "will answer", "had answered"], 1, "Third Conditional: if + had V3, would have + V3."),
        ("If I ___ about it 5 years ago, I wouldn't have believed it.", ["heard", "had heard", "have heard", "would hear"], 1, "Условие в прошлом → Past Perfect."),
        ("If I had watched lots of documentaries, I ___ very smart now.", ["would be", "would have been", "will be", "am"], 0, "Mixed: условие в прошлом, результат в настоящем."),
        ("Форма Third Conditional:", ["if + Past Simple, would + V", "if + Past Perfect, would have + V3", "if + Present, will + V", "if + Past Perfect, will + V"], 1, "if + had V3, would have + V3."),
    ],
    gap=(["had been", "would have liked", "had had"], [
        ("If the atmosphere ", ["had been"], " more fun, you would have liked it more."),
        ("If the party had been more fun, you ", ["would have liked", "would've liked"], " it more."),
        ("If I ", ["had had"], " money, I would've bought a car."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["If I had known, I would have come.", "If I would have known, I had come.", "If I had bought stocks, I would be richer now.", "If she had studied, she would have passed.", "If I knew it yesterday, I would have told you."],
           [0, 2, 3], "Условие о прошлом — had + V3 (had known)."),
),
15: dict(
    mcq=[
        ("You ___ enter the lab without safety goggles. (запрещено)", ["don't have to", "must not", "aren't supposed", "needn't"], 1, "Запрет: mustn't = can't = be not allowed."),
        ("We ___ wear formal clothes — it's a casual dress code.", ["mustn't", "don't have to", "can't", "aren't allowed"], 1, "don't have to — нет необходимости."),
        ("Обязанность извне (правила, начальник):", ["must", "have to", "should", "can't"], 1, "have to — обязанность извне; must — часто внутренняя."),
        ("You ___ scare visitors, but you mustn't bite them.", ["are supposed to", "must not", "don't have to", "can't"], 0, "be supposed to — от вас ожидается."),
    ],
    gap=(["have to", "shouldn't", "mustn't"], [
        ("I ", ["have to"], " be at work at 9 — my boss is strict."),
        ("You ", ["shouldn't", "should not"], " bring your phone to the interview — it's not recommended."),
        ("Employees ", ["mustn't", "must not"], " eat at their desks — it's against the rules."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["You must not enter the lab without goggles.", "We don't have to hand in the report until next week.", "I'm not supposed to arrive before 9.", "You don't have to smoke here — it's forbidden.", "She have to work on Saturdays."],
           [0, 1, 2], "Для запрета нужен mustn't, не don't have to. She has to."),
),
16: dict(
    mcq=[
        ("I failed the interview. I ___ for it.", ["should prepare", "should have prepared", "could prepare", "must prepare"], 1, "Сожаление о прошлом: should have + V3."),
        ("«Могла бы ответить» →", ["should've answered", "could've answered", "would answer", "must have answered"], 1, "could have + V3 — возможность, которой не воспользовались."),
        ("You ___ talked more about your hard skills.", ["should've", "should", "could", "must"], 0, "should've + V3 — надо было."),
        ("The show ___ have been canceled. (жаль, что отменили)", ["should", "shouldn't", "couldn't", "mustn't"], 1, "shouldn't have + V3 — не стоило."),
    ],
    gap=(["should have prepared", "could have lied", "shouldn't have mentioned"], [
        ("I ", ["should have prepared", "should've prepared"], " better for the interview."),
        ("You ", ["could have lied", "could've lied"], " about the croissants!"),
        ("He ", ["shouldn't have mentioned", "should not have mentioned"], " his salary so early."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["I should have called you.", "You could've told me!", "I should called you yesterday.", "She shouldn't have said that.", "We could have went there."],
           [0, 1, 3], "Форма: modal + have + V3 (called, gone)."),
),
17: dict(
    mcq=[
        ("«Ты наверняка это видел» →", ["You must have seen it.", "You should have seen it.", "You must see it.", "You had seen it."], 0, "must have + V3 — почти уверены."),
        ("«Возможно, ты это видел» →", ["You might have seen it.", "You might seen it.", "You might to have seen it.", "You might saw it."], 0, "might have + V3 — возможно."),
        ("Форма предположения о прошлом:", ["modal + have + V3", "modal + V2", "modal + had + V3", "modal + to + V"], 0, "Modal + have + V3."),
        ("She isn't answering. She ___ fallen asleep.", ["might have", "might", "must", "should"], 0, "might have fallen — возможно, уснула."),
    ],
    gap=(["must have seen", "might have heard", "must have forgotten"], [
        ("Everyone knows this film. You ", ["must have seen"], " it."),
        ("I'm not sure, but she ", ["might have heard"], " the news."),
        ("He isn't here. He ", ["must have forgotten"], " about the meeting."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["You must have seen it.", "You might have seen it.", "You must have saw it.", "She might have missed the train.", "He must has forgotten."],
           [0, 1, 3], "После modal — have + V3 (seen, forgotten)."),
),
18: dict(
    mcq=[
        ("The more you practise, ___ you become.", ["the better", "better", "the best", "more better"], 0, "Parallel comparatives: the + comparative, the + comparative."),
        ("This flat is ___ more expensive than that one.", ["slightly", "the most", "very", "more"], 0, "Quantifiers с comparative: slightly more expensive."),
        ("He is by far ___ talented student.", ["the most", "more", "most", "the more"], 0, "by far + superlative."),
        ("The roads are getting ___.", ["more and more dangerous", "more dangerous and dangerous", "most and most dangerous", "dangerous and dangerous"], 0, "Повтор comparative подчёркивает изменение."),
    ],
    gap=(["than ever", "as", "the more"], [
        ("We've had more forest fires this year ", ["than ever"], " before."),
        ("This town isn't ", ["as"], " busy as London."),
        ("The bigger the project, ", ["the more"], " responsibilities I have."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["The more I work, the more I understand.", "He drives more quietly than me.", "It's the most cheapest option.", "This is the tallest building ever.", "My English is more better now."],
           [0, 1, 3], "Не сочетаем more/most с -er/-est: the cheapest, better."),
),
19: dict(
    mcq=[
        ("I turn off my phone ___ get distracted.", ["so as not to", "so not to", "in order to not", "for not"], 0, "Отрицание: so as not to / in order not to."),
        ("She's learning memes ___ her colleagues laugh at her jokes.", ["to", "in order to", "so that", "so as to"], 2, "Разные подлежащие → so that."),
        ("I'm learning English ___ get into a university.", ["in order to", "so that", "for", "in order that"], 0, "Одно подлежащее → to / in order to + глагол."),
        ("He set an alarm ___ oversleep.", ["in order not to", "not in order to", "so that not", "for not to"], 0, "not ставится перед to."),
    ],
    gap=(["so that", "to", "so as not to"], [
        ("I'd like to move closer to the stage ", ["so that"], " I can hear better."),
        ("I'm going downstairs ", ["to", "in order to"], " lock up."),
        ("I check my to-do list every day ", ["so as not to", "in order not to"], " forget anything."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["I eat vegetables to improve my health.", "She saved money in order to buy a car.", "I study hard in order to my parents are proud.", "Let's check it so that we don't make a mistake.", "He left early for not to be late."],
           [0, 1, 3], "Если подлежащие разные — so that (so that my parents are proud)."),
),
20: dict(
    mcq=[
        ("I can't resist ___ new things.", ["buy", "buying", "to buy", "bought"], 1, "can't resist + V-ing."),
        ("If you can't sleep, try ___ warm milk. (как эксперимент)", ["drinking", "to drink", "drink", "drunk"], 0, "try + -ing — попробовать как эксперимент."),
        ("We stopped ___ lunch. (остановились, чтобы пообедать)", ["having", "to have", "have", "had"], 1, "stop + to — прервать одно, чтобы сделать другое."),
        ("I'm looking forward to ___ you.", ["see", "seeing", "saw", "seen"], 1, "look forward to + V-ing."),
    ],
    gap=(["finding", "to open", "smoking"], [
        ("I finally succeeded in ", ["finding"], " a job."),
        ("I tried ", ["to open"], " the door, but it was locked."),
        ("He stopped ", ["smoking"], " last year."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["She apologised for getting angry.", "We carried on driving.", "I'm thinking about change my job.", "I ended up carrying another plant home.", "She dreams about become a doctor."],
           [0, 1, 3], "После предлога — V-ing: about changing, about becoming."),
),
21: dict(
    mcq=[
        ("___ the fact that you don't do homework, you aren't progressing.", ["Due to", "Because", "Despite", "Lead to"], 0, "Due to the fact that + clause — из-за того, что."),
        ("Binge-watching can ___ sleep problems.", ["lead to", "due to", "despite", "because"], 0, "lead to — привести к (следствие)."),
        ("The flight was cancelled due to ___.", ["the storm", "it was stormy", "of the storm", "that storm was"], 0, "Due to + noun."),
        ("___ the fact that it was raining, we went for a walk.", ["Despite", "Due to", "Because of", "Lead to"], 0, "despite the fact that — несмотря на то что."),
    ],
    gap=(["due to", "cause", "despite the fact that"], [
        ("The match was cancelled ", ["due to"], " bad weather."),
        ("Too much screen time can ", ["cause", "lead to"], " psychological problems."),
        ("We carried on walking ", ["despite the fact that"], " it was raining."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["Due to the situation, we stayed home.", "Due to it rained, we stayed home.", "It can lead to significant consequences.", "Despite the fact that he was tired, he finished the report.", "It can cause to problems."],
           [0, 2, 3], "Due to + noun или due to the fact that + clause. cause без to."),
),
22: dict(
    mcq=[
        ("I'd rather ___ her a message than phone her.", ["send", "to send", "sending", "sent"], 0, "would rather + глагол без to."),
        ("Would you prefer ___ rich or famous?", ["to be", "be", "being", "been"], 0, "would prefer + to + глагол."),
        ("Would you rather ___ tea or coffee?", ["have", "to have", "having", "had"], 0, "Would you rather + глагол без to."),
        ("I'd definitely prefer ___ at the options first.", ["to look", "look", "looking at to", "looked"], 0, "I'd prefer to…"),
    ],
    gap=(["rather", "prefer to", "would"], [
        ("I'd ", ["rather"], " stay at home tonight."),
        ("I'd ", ["prefer to"], " look at the options before deciding."),
        ("", ["would"], " you rather live in the city or in the countryside?"),
    ]),
    multi=("Какие предложения построены правильно?",
           ["I'd rather stay.", "Would you prefer to be rich?", "I'd rather to go home.", "Would you rather have tea?", "I'd prefer go now."],
           [0, 1, 3], "rather — без to, prefer — с to."),
),
23: dict(
    mcq=[
        ("___ a storm tomorrow.", ["There will be", "It will be", "Will be", "There is going"], 0, "Существование чего-то → There + be + noun."),
        ("___ rainy tomorrow.", ["It will be", "There will be", "Will be", "It will"], 0, "Описание → It + be + adjective."),
        ("There ___ be someone between me and a developer.", ["should", "should to", "is should", "shoulds"], 0, "There + modal + be."),
        ("There + be + ___ — о существовании чего-то.", ["noun", "adjective", "verb", "adverb"], 0, "There + be + noun; It + be + adjective."),
    ],
    gap=(["There will be", "It will be", "There must be"], [
        ("Scientists say ", ["there will be"], " an earthquake soon."),
        ("", ["it will be"], " cold and windy tomorrow."),
        ("", ["there must be"], " a mistake — I didn't order this."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["There will be a storm.", "It will be rainy.", "It will be a storm.", "There should be a manager here.", "There will be rainy."],
           [0, 1, 3], "С существительным — there, с прилагательным — it."),
),
24: dict(
    mcq=[
        ("Susan thinks Ben doesn't like jazz, but he ___.", ["does", "is", "likes", "do"], 0, "Вспомогательный глагол заменяет весь глагол: he does."),
        ("Are you going to the party? — I think ___.", ["so", "it", "yes", "that"], 0, "think so — положительный ответ."),
        ("Has Angus gone home? — I hope ___.", ["not", "no", "don't", "so not"], 0, "Отрицание: hope not, suppose not, guess not."),
        ("My parents expected me to go to college, but I didn't want ___.", ["to", "it", "so", "that"], 0, "want to заменяет глагол."),
    ],
    gap=(["did", "I'd love to", "I'll try not to"], [
        ("I didn't see John, but Mary ", ["did"], "."),
        ("Would you like to go out tonight? — Yes, ", ["i'd love to", "i would love to"], "."),
        ("Don't work too hard. — ", ["i'll try not to", "i will try not to"], "."),
    ]),
    multi=("Какие предложения построены правильно?",
           ["I don't think so.", "I hope not.", "I think not so.", "I'd like to be, but it's not easy.", "I suppose yes."],
           [0, 1, 3], "Говорят: I don't think so, I suppose so."),
),
}
