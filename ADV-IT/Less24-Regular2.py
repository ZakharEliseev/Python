import re
input_file = '1py.txt'
ressult_file = 'results.txt'

inputfile = open(input_file, mode='r', encoding='Latin-1')
resultfile = open(ressult_file, mode='w', encoding='Latin-1')

mytext = inputfile.read()

lookfor = r'[\w.-]+@?[\w]+\.[\w]+'

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + '\n')
print(str(len(results)))