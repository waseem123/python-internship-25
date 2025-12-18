# list is a mutable, indexed, orderd collection of data with unique as well as repeated values

mylist = [100,200,300,400,500,200,400]
print(mylist)
print(len(mylist))
print(type(mylist))

cities = ['Solapur','Pune','Mumbai','Bengaluru','Delhi']
print(cities)

print(mylist[0])
print(cities[2])


datalist = list(("a","b","c","d"))
print(datalist)

demo = list(mylist)
print(demo)

for i in mylist:
    print(i)

for i in cities:
    print(i)