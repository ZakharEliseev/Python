import random

import telebot

token = '1972623839:AAEacDtL6ohqar2jYjT3-oLeMIcUngDIUII'

bot = telebot.TeleBot(token)
HELP = """
/help - Справка по командам бота
/add - Добавление задачи 
/show - Добавленные задачи
/show_all - Показать все задачи без дат
/exit - exit
/random - add random task for date
"""
tasks = {}
random__tasks = ['Learn Python', 'Create Telegram bot', 'Create parser', 'Rod to DevOps']


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = 'Task ' + task + ' added to date ' + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['random'])
def random_add(message):
    date = 'today'
    task = random.choice(random__tasks)
    add_todo(date, task)
    text = 'Task ' + task + ' added to date ' + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['show', 'print'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ''
    if date in tasks:
        text = date.upper() + '\n'
        for task in tasks[date]:
            text = text + '[] ' + task + '\n'
    else:
        text = 'Tasks not for date'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['show_all'])
def show_all(message):
    all_tasks = tasks.items()
    bot.send_message(message.chat.id, all_tasks)


bot.polling(none_stop=True)
