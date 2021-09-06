cities = ["New york", "Moscow", "new dehli", "Simfferopol", "Toronto"]
print(cities)
print(len(cities))
print(cities[-2])
print(cities[2].title())
cities[2] = "Tula"
print(cities)
cities.append("Kursk")
cities.append("Yalta")
print(cities)
cities.insert(2, "Feodosiya")
print(cities)

del cities[-1]
print(cities)

cities.remove("Tula")
print(cities)

deleted_city = cities.pop()
print(deleted_city)
print(cities)

cities.sort(reverse=True)
print(cities)

cities.sort()
print(cities)

cities.reverse()
print(cities)