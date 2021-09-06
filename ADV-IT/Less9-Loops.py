'''x = 25

if x == 25:
    print("Yes, x = " + str(x))
else:
    print("No")

print("_________________________")

age = 20
if age <= 4:
    print("You baby")
elif (age > 4) and (age < 12):
    print("You kid")
elif (age >= 12) and (age < 19):
    print("You teen")
else:
    print("You old")
print("_________________________")

all_cars = ['crusler', 'dacia', 'bmw', 'KIA', 'vw', 'seat' , 'skodda' , 'lada', 'audi', 'dord', 'Chevrolett']
german_cars = ['bmw', 'vw', 'audi']

if 'lada' in all_cars:
    print("Yes, lada in the list")
else:
    print('No')
print("_________________________")'''
all_cars = ['crusler', 'dacia', 'bmw', 'KIA', 'vw', 'seat' , 'skoda' , 'lada', 'audi', 'ford', 'Chevrolet']
german_cars = ['bmw', 'vw', 'audi']
for x in all_cars:
    if x in german_cars:
        print(x + ' is german cars')
    else:
        print(x + ' Not german car')

print("_________________________")
'''for x in all_cars:
    if x in german_cars:
        print(x + ' is german cars')'''