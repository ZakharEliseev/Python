import re
from _ast import While

mytext = 'aasasasd aaaaaa 1972. Kolya - 1972: Olesya 192823, wsdkl;sdkl;dfkl;@kl;dfkl;dfkl;df.com'\
         'Vasya aaaaaa 1972. xxxxx - 1972: Olesya 192823, wsdkl;sdkl;dfkl;@kl;dfkl;dfkl;df.com'\
         '12121212 aaaaaa 1972. 234432 - 1972: dfdfdfssdfs3 192823, wsdkl;sdkl;dfkl;@kl;dfkl;dfkl;df.com'\
         'Vasya aaaaaa 1972. Kolya - 1972: Olesya 192823, wsdkl;sdkl;dfkl;@kl;dfkl;dfkl;df.com'\
         'asddfef aaaaaa 1972. Kolya - 1972: 55555 192823, wsdkl;sdkl;dfkl;@kl;dfkl;dfkl;df.com'

'''
\d = Any Digit 0-9
\D = Any nnon DIGIT
\w = Any Alpfabet symbol a - z, A - Z
\W = any non Alphabet symbol
\s = breakspace
\S = Non Breakspace


'''


textlookfor = r'\d\d\d'
allresults = re.findall(textlookfor, mytext)

print(allresults)

a = "Learn Python: action in progress..."
b = "Learn Python: action completed."

year = input()
month = input()
day = input()
info = "Дата рождения пользователя:"
print(info + ' ' + year + " - " + month + " - " + day)
