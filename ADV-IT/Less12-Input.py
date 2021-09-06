#name = input('Enter u name: ')
#print('Your name' + name)
#n1 = input('Enter x: ')
#n2 = input('Enter y: ')
#summa = int(n1) + int(n2)
#print(summa)

mylist = []
mag = ''
while mag != 'stop':
    mag = input('Enter new item and STOP to finish')
    mylist.append(mag)

print(mylist)


'''
cc
while True:
    messg = input('Enter u pswd: ')
    if messg == 'secret':
        break
    print(messg + ' Password not correct!')
    
print(messg + " PSWD is valid")
'''