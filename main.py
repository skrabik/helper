import json

import datetime

import requests
from entitys import Message
from url import *
from env import *

stack = []

while True:

    dt = datetime.datetime.now().replace(second=0, microsecond=0)
    if dt in tasks:
        requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Задача через 30 мин: \n {tasks[dt]}')
        del tasks[dt]

    try:
        update = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={str(OFFSET)}')
    except:
        continue
    if len(update.json()['result']) != 0:
        try:
            message = Message(update)
        except:
            send_message('Неверный формат')
            OFFSET += 1
            continue

        if message.user == USERNAME:
            stack.append(message)
        else:
            continue

        if stack:

            OFFSET += 1
            answer = 'Непонял'
            if message.text in db:
                OFFSET = db[message.text](offset=OFFSET)
            else:
                try:
                    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={message.chat_id}&text={answer}")
                    print('Ответ успешно отправлен')
                except:
                    print('Ответ не был отправлен')

            with open('last_offset.txt', 'w') as f:
                f.write(str(OFFSET))