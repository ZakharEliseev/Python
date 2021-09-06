def napechatat_privetstvie(name):
    """SykaBlyad"""
    print('Congrat!' + name)
    print('Hello')


def a(bbb):
    print('aaaa' + bbb)


print('____')

napechatat_privetstvie('Den')
napechatat_privetstvie('Vas')
a('vvv')
print('____')
print(napechatat_privetstvie('123'), a('123'))
print('____')


def summa(x, y):
    print(x + y)


summa(10, 20)
print('____')


def summa1(x, y):
    s = (x + y)
    return s


x = summa1(33, 22)
print(x)
print('____')


def summa1(x, y):
    return x + y


print(summa1(100, 50))
print('____')

def fact(x):
    '''Calc fact x'''
    otvet = 1
    for i in range(1, x + 1): # перемножает заданное число от 1 до самого себя, так как в range последнее число всегда -1, то пишем х + 1 чтобы получить отправленное число
        otvet = otvet * i
    return otvet

print('____')
for i in range(1, 10):
    print(str(i) + '!\t = ' + str(fact(i) ))

print('____')
print(fact(1))
print(fact(4))




