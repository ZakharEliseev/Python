cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
print(cars)
for car in cars:
    print(car.upper())

for car in range(1,6):
    print(car)

number_list = list(range(0, 10))
print(number_list)


print("___________________________")

for x in number_list:
    x = x * 2
    print(x)

number_list.sort(reverse=True)
print("My number list is  " + str(number_list))
print("Max number list is  " + str(max(number_list)))
print("Min number list is  " + str(min(number_list)))
print("Max number list is  " + str(sum(number_list)))
print("___________________________")
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
mycars = cars[1:4]
print(mycars)
mycars = cars[:4]
print(mycars)
mycars = cars[-3:-1]
print(mycars)
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
mycars = cars[:]