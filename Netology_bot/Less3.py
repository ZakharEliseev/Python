HELP = """
help - spravka
add - dobavlenie
show - pokazat dobavlenie
exit - exit
"""
run = True
task_today = []
task_tomorrow = []
task_other = []
while run:
    command = input('введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'add':
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        if date == 'today':
            task_today.append(task)
            print('Congrats! You added task is: ', task, 'for', date)
        elif date == 'tomorrow':
            task_tomorrow.append(task)
            print('Congrats! You added task is: ', task, 'for', date)
        elif date == 'other':
            task_other.append(task)
            print('Congrats! You added task is: ', task, 'for', date)
    elif command == 'show':
        print(task_today)
        print(task_tomorrow)
        print(task_other)
    elif command == 'exit':
        print('Good day, by')
        break
    else:
        print('Unknown command!')
        #run = False
        break
print('Bue')


