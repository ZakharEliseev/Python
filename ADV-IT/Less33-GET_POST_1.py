from urllib import request
from urllib import request, parse
import sys
'''
myURL = 'https://www.astahov.net'
otvet = request.urlopen(myURL)

mytext1 = otvet.readlines()
mytext2 = otvet.read()

print(otvet)
print(mytext2)
for line in mytext1:
    print(line)

'''
'''
myURL = 'http://www.google.com/search?'
value = {'q':'ANDESSA Soft'}

myheaders = {}
myheaders['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myURL = myURL + mydata
    req = request.Request(myURL, headers=myheaders)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)
except Exception:
    print('Error occuried during web req!')
    print(sys.exc_info()[1])
'''

myURL = 'https://adv400.tripod.com/kartinka.jpg'
myfile = '/home/ezv/Загрузки/mykartinka.jpg'

try:
    print('Start Downloaidng File from: ' + myURL)
    request.urlretrieve(myURL, myfile)
except Exception:
    print('AHTUNG!!!')
    print(sys.exc_info())
    exit()
print('File Downloaded and saved at: ' + myfile)


