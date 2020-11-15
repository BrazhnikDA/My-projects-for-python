import json
from datetime import datetime

# VK_API
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id

# Авторизация
vk_session = VkApi(token='d369c2092f583d5cea4d73f0fdebfdd110fbde25170939e11b94c891d3b5754c5d9d249b7423c41b790d7')
long_poll = VkBotLongPoll(vk_session, '198500891')
vk = vk_session.get_api()
upload = VkUpload(vk)

# Переменные для статистики
with open("statistics.txt", "r+") as file:
    today = int(file.readline())
    print("Сегодня:", today, end="\n")
    tomorrow = int(file.readline())
    print("Завтра:", tomorrow, end="\n")
    week = int(file.readline())
    print("Вся неделя:", week, end="\n")
    call = int(file.readline())
    print("Расписание звонков:",call, end="\n")
    eror = int(file.readline())
    print("Ошибки:", eror)
file.close()

# Перезапись файла
def reWrite():
    with open("statistics.txt", "r+") as file:
        file.write(str(today) + '\n' + str(tomorrow) + '\n' + str(week) + '\n' + str(call) + '\n' + str(eror))

# Получаем день недели (1-7)
def get_day():
    return datetime.today().isoweekday()

# Отправить расписание на сегодня или ЗАВТРА
def send_raspisanie_today(sdvig):
    day = get_day()
    day += sdvig
    # Если Сегодня 7 день,то +1 даст 8 день, перебрасываем его на первый день
    if (day == 8):
        day = 1
    if day == 1:
        vk.messages.send(
            peer_id=peer_id,
            keyboard=keyboard,
            message="Понедельник: \n1) Технология (1-4)\n2) Технология (1-4)\n3) МПМ (1-2)\n4) МПМ (1-2)\n5) Физическая культура\n6) Физизическая культура\n7) Педагогика (2-15)\n8) Педагогика (2-15)",
            random_id=get_random_id(),
        )
    if day == 2:
        vk.messages.send(
            peer_id=peer_id,
            keyboard=keyboard,
            message="Вторник: \nОтдыхаем",
            random_id=get_random_id(),
        )
    if day == 3:
        vk.messages.send(
            peer_id=peer_id,
            keyboard=keyboard,
            message="Среда: \n1) Русский язык (2-16)\n2) Русский язык (2-16)\n3) МПР (2-16)\n4) МПР (2-16)\n5) Педагогика (2-4)\n6) ТОМ (3-15)\n7) Детская литература (2-16)\n8) ИКТ (3-10, 3-9)\n9) МДК (01-01) \n",
            random_id=get_random_id(),
        )
    if day == 4:
        vk.messages.send(
            peer_id=peer_id,
            keyboard=keyboard,
            message= "Четверг: \n1) ИЗО (1-5)\n2) ИЗО (1-5)\n3)  БЖ (2-10А)\n4) БЖ (2-10А)\n5) ИКТ (3-10)\n6) Педагогика (3-2)\n7) МПМ (1-2)\n8) МПМ (1-2)",
            random_id=get_random_id(),
        )
    if day == 5:
        vk.messages.send(
            peer_id=peer_id,
            keyboard=keyboard,
            message="Пятница: \n1) МПР (2-16)\n2) МПР (2-16)\n3) МДК (01-01)\n4) Иностранный язык (1 - 1-17, 2 - 3-19)\n5) Иностранный язык (1 - 1-17, 2 - 3-19)\n6) ТОМ (3-15)\n7) ТОМ (3-15)",
            random_id=get_random_id(),
        )
    if day == 6:
        vk.messages.send(
            peer_id=peer_id,
            keyboard=keyboard,
            message="Суббота: \n1) Дем. лит (2-16)\n2) Детская литература (2-16)\n3) Русский язык (2-16)\n4) Русский язык (2-16)",
            random_id=get_random_id(),
        )
    if day == 7:
        vk.messages.send(
            peer_id=peer_id,
            keyboard=keyboard,
            message="Воскресенье:\nСегодня точно отдыхаем",
            random_id=get_random_id(),
        )

# Отправить расписание на всю неделю
def all_raspisanie():
    str = "Понедельник: \n1) Технология (1-4)\n2) Технология (1-4)\n3) МПМ (1-2)\n4) МПМ (1-2)\n5) Физическая культура\n6) Физизическая культура\n7) Педагогика (2-15)\n8) Педагогика (2-15)\n\n" \
          "Вторник: \nОтдыхаем\n\n" \
          "Среда: \n1) Русский язык (2-16)\n2) Русский язык (2-16)\n3) МПР (2-16)\n4) МПР (2-16)\n5) Педагогика (2-4)\n6) ТОМ (3-15)\n7) Детская литература (2-16)\n8) ИКТ (3-10, 3-9)\n9) МДК (01-01) \n\n" \
          "Четверг: \n1) ИЗО (1-5)\n2) ИЗО (1-5)\n3)  БЖ (2-10А)\n4) БЖ (2-10А)\n5) ИКТ (3-10)\n6) Педагогика (3-2)\n7) МПМ (1-2)\n8) МПМ (1-2)\n\n" \
          "Пятница: \n1) МПР (2-16)\n2) МПР (2-16)\n3) МДК (01-01)\n4) Иностранный язык (1 - 1-17, 2 - 3-19)\n5) Иностранный язык (1 - 1-17, 2 - 3-19)\n6) ТОМ (3-15)\n7) ТОМ (3-15)\n\n" \
          "Суббота: \n1) Дем. лит (2-16)\n2) Детская литература (2-16)\n3) Русский язык (2-16)\n4) Русский язык (2-16)\n\n" \
          "Воскресенье:\nСегодня точно отдыхаем\n"

    vk.messages.send(
        peer_id=peer_id,
        keyboard=keyboard,
        message=str,
        random_id=get_random_id(),
    )

# Отправить расписание звонков
def call_raspisanie():
    str = "Расписание звонков:\n1) 8:30 - 9:15 (5 мин.)\n2) 9:20  - 10:05 (5 мин.)\n3) 10:10 - 10:55 (5 мин.)\n4) 11:00 - 11:45 (10 мин.)\n5) 11:55 - 12:40 (30 мин.)\n6) 13:10 - 13:55 (5 мин.)\n7) 14:00 - 14:45 (5 мин.)\n8) 14:50 - 15:35 (10 мин.)\n9) 15:45 - 16:30"

    vk.messages.send(
        peer_id=peer_id,
        keyboard=keyboard,
        message=str,
        random_id=get_random_id(),
    )

# Создать кнопку
def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

# Отображение клавиатуры
keyboard = {
    "one_time": False,
    "buttons": [
        [
            get_button(label="Сегодня", color="positive")
        ],
        [
            get_button(label="Завтра", color="default"),
            get_button(label="Вся неделя", color="default")
        ],
        [
            get_button(label="Расписание звонков", color="primary")
        ]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

# Прослушивание чатас
for event in long_poll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.obj['message']

        peer_id = message['peer_id']
        text = message['text']
        str(text)
        s = text.lower()
        with open("statistics.txt", "r+") as file:

            if s == "начать":
                vk.messages.send(
                    peer_id=peer_id,
                    keyboard=keyboard,
                    message="Привет!\nС помощью этого бота ты можешь узнать актуальное расписание.",
                    random_id=get_random_id(),
                )
            elif s == "сегодня":
                today += 1
                reWrite()
                send_raspisanie_today(0)
            elif s == "завтра":
                tomorrow += 1
                reWrite()
                send_raspisanie_today(1)
            elif s == "вся неделя":
                week += 1
                reWrite()
                all_raspisanie()
            elif s == "расписание звонков":
                call += 1
                reWrite()
                call_raspisanie()
            else:
                eror += 1
                reWrite()
                vk.messages.send(
                    peer_id=peer_id,
                    keyboard=keyboard,
                    message="Я тебя не понимаю!",
                    random_id=get_random_id(),
                )
