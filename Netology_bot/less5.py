import random
import telebot



HELP = """
help - spravka
add - dobavlenie
show - pokazat dobavlenie
exit - exit
random - add random task for date
"""


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print('Congrats! You added task is: ', task, 'for', date)


run = True
tasks = {}

while run:
    command = input('введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'add':
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        add_todo(date, task)
    elif command == 'show':
        date = input('Enter date for display tasks: ')
        if date in tasks:
            for task in tasks[date]:
                print('-', task)
        else:
            print('Wrong date')
    elif command == 'exit':
        print('Good day, by')
        break
    elif command == 'random':
        task = random.choice(random__tasks)
        add_todo('today', task)
    else:
        print('Unknown command!')
        # run = False
        break
