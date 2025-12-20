cities = ['Solapur','Pune','Mumbai','Bengaluru','Delhi']
print(cities)

cities.append("Kolkata")
print(cities)

cities.append('Hyderabad')
print(cities)

cities.insert(0,"Chennai")
print(cities)


cities.insert(4,"Vijaypur")
print(cities)

cities.insert(100,'Jaipur')
print(cities)
print("___________________________________")

cities[5] = 'Bangalore'
print(cities)

# cities[300] = 'Bombay'
# print(cities)
print("___________________________________")

cities = ['Vijaypur','Chennai', 'Solapur', 'Vijaypur','Pune', 'Mumbai', 'Vijaypur', 'Bangalore', 'Delhi', 'Kolkata', 'Hyderabad', 'Jaipur']
print(cities)
cities.pop()
print(cities)
cities.pop()
print(cities)

cities.pop(2)
print(cities)

cities.remove('Vijaypur')
cities.remove('Vijaypur')
print(cities)

del cities[2]
print(cities)

cities.clear()
print(cities)

del cities
# print(cities)
print("_______________________")


l1 = ['C','C++','Java']
l2 = ['Python','C#','Javascript','Dart']

l3 = l2 + l1
print(l3)
l2.extend(l1)
print(l1)
print(l2)
print("@___________________")
print(l1*40)