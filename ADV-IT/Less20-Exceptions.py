import sys

filename = "Lesson_List.txt"

'''
myfile = open(filename, mode='r', encoding='Latin-1')
print(myfile.read())
'''
while True:
    try:
        print('Insade try')
        myfile = open(filename, mode='r', encoding='Latin-1')
    except Exception:
        print("Inside EXCEPT")
        print('Error Found!')
        print(sys.exc_info()[1])
        filename = input('Enter correct file name')
    else:
        print('Inside else')
        print(myfile.read())

    finally:
        print('Inside Finaly')
        
print('________________________________')