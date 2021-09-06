#name = input('Vvedite imya: ')
#print(name)
#name1 = 'Dima'
#print(name == name1)
name = input('Vvedite imya: ')
login = 'Dima'

if name == login:
    print('Hello,', name)
elif len(name) < 3:
    print('NOT!')
elif name == 'Yo':
    print('Yo, bro')
else:
    print('Hello, user!')