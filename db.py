import requests

from entitys import *
from env import *
from get_date import *

tasks = dict()

def send_message(text):
    try:
        requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}')
    except:
        send_message(text)
    return

def get_answer(offset):
    while True:
        try:
            update = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={str(offset)}')
        except:
            continue
        if len(update.json()['result']) != 0:
            message = Message(update)
            text = message.text
            offset += 1
            break
    return offset, text


def add_task(offset):
    send_message('Введите дату выполнения задачи\nФормат: месяц дата час мин')
    offset, date = get_answer(offset)
    try:
        dt_task = get_date_in_advance(date)
    except:
        send_message('Неверный формат даты и времени')
        return offset + 1
    send_message('Что запланировано?')
    offset, text = get_answer(offset)
    tasks[dt_task] = text
    send_message('Задача успешно добавлена!')
    return offset

def hi(offset):
    send_message('Команды:\n/add_task\n/get_all_task\n/del_task')
    return offset

def get_all_tasks(offset):
    if tasks:
        number = 1
        rez = ''
        for i in tasks:
            rez += f'{number}) '
            rez += i.strftime('%m/%d/%y %H:%M') + ': '
            rez += tasks[i]
            rez += '\n'
            number += 1
        send_message(rez)
    else:
        send_message('Список задач пуст')
    return offset

def del_task(offset):
    send_message('Введите номер задачи')

    offset, text = get_answer(offset)

    if int(text) > len(tasks):
        send_message('Такого номера задачи нет')
        return offset
    c = 1
    for i in tasks:
        if c == int(text):
            del tasks[i]
            break
        c += 1
    send_message(f'задача {c} успешно удалена')
    return offset
