import sys
import os
'''
print('Hello ')

print(sys.argv[1:])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
'''
x = len(sys.argv)
if x > 1:
    if sys.argv[1] == '/?':
        print('Help Requested')
        print('Usage of this program is python.exe')
    print('Arguments entered: ' + str(sys.argv[1:]))
else:
    print('Arguments NOT PROVIDED')

os.system('ls > test.txt')
#os.mkdir('my dir')
sys.exit(2)