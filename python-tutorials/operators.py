a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print("_______________________")
a = 10
b = 5
c = b
print(a,b,c)
a += b # a = a + b
print(a)

a -= c # a = a - c
print(a)

a *= 2
print(a)

a /= 2
print(a)
print("_______________________")

a = 20.0
b = 20
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)
print("_______________________")

a = 100
b = 25
print(a>b and a>88)
print(a>b and a>1000)
print(a<b and a>88)
print(a<b and a>200)
print(a>b or a>88)
print(a>b or a>1000)
print(a<b or a>88)
print(a<b or a>200)
print(not(a<b or a>88))
print(a<b or not(a>200))
print("_______________________")

a = 5
b = 3
print(a&b)
print(a|b)
print("_______________________")

a = 2
b = 2
print(a<<b)
print(a>>b)
print("_______________________")

a = 500
print(type(a) is int)
print(type(a) is float)
print(type(a) is not int)
print(type(a) is not str)
print("_______________________")

cities = ['Solapur','Pune','Chennai','Delhi','Mumbai']
print('Solapur' in cities)
print('London' in cities)
print('Hyderabad' not in cities)
print('Chennai' not in cities)
# 0101
# 0011
# _________
# 0001