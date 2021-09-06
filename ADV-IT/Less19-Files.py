"""
inputfile = '/home/mfclsptop/PyFile/PyFiles/user_names.txt'

myfile = open(inputfile, mode='r', encoding='utf_8')

# print(myfile.read())

for num, line in enumerate(myfile, 1):
    if 'Александр' in line:
        print(str(num) + " Hello " + line.strip())
"""
inputfile = '/home/mfclsptop/PyFile/PyFiles/list_of_passwords.txt'
outputfile = '/home/mfclsptop/PyFile/PyFiles/passwords.txt'



myfile1 = open(inputfile, mode='r', encoding='utf_8')
myfile2 = open(outputfile, mode = 'a', encoding = 'utf_8')
# print(myfile.read())

password_tolookfor = 'kls'

for num, line in enumerate(myfile1, 1):
    if password_tolookfor in line:
        print('Line is: ' + str(num) + ' : '+  line.strip())
        myfile2.write('Found password ' + '    :   ' + line)

myfile1.close()
myfile2.close()
