# Tuples are indexed oredered and immutable collection of data with repeated and unrepeated values

mytuple = (100,200,300,400,500,600)
print(mytuple)
print(type(mytuple))
print(len(mytuple))

demo = tuple(('Charger','smartwatch','Mobile Phone','TV'))
print(demo)
print(type(demo))
print(len(demo))

print(demo[2])
print(demo[3])
print("_________________________")
for i in mytuple:
    print(i)
print("_________________________")

# mytuple.insert(0,900)
# mytuple[2] = 50
# del mytuple[3]
# mytuple.clear()
del mytuple
# print(mytuple)
print("_________________________")

demo = ('Alex','Peter','Bob','John','Sam')
(*doctor,engineer,soldier,police) = demo
print(doctor)
print(engineer)
print(soldier)
print(police)
# print(singer)