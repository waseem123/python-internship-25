myset = {100,200,300,400,500}
print(myset)

myset = {'Saniya','Misbah','Sanobar','Madiha'}
print(myset)
# print(myset[0])
print(type(myset))

demo = set(('Mobile','Watch','Television','Laptop','Watch','Television','Earbuds','Television','Charger','Power Bank'))
print(demo)
print(len(demo))

for i in myset:
    print(i)

print("_________________________________")

myset = {'Saniya','Misbah','Sanobar','Madiha','Falak'}
print(myset)
myset.add('Kulsum')
print(myset)
myset.update({'Hajra','Lubna'})
print(myset)
# myset[3]='Misbah Sayyed'
print("_________________________________")
myset.pop()
print(myset)

myset.remove('Lubna')
print(myset)

myset.discard('Alice')
print(myset)

myset.clear()
print(myset)

del myset
# print(myset)

print("-------------------------")

s1 = {'Whatsapp','Snapchat','Instagram','Myntra'}
s2 = {'Amazon','Flipkart','Meesho','Snapchat','Instagram','Myntra'}
s3 = s1.union(s2)
print(s3)
s4 = s1.intersection(s2)
print(s4)
s5 = s1.difference(s2)
print(s5)
s6 = s2-s1
print(s6)
s7 = s1.symmetric_difference(s2)
print(s7)


s0 = {'Snapchat', 'Instagram', 'Myntra', 'Flipkart', 'Meesho', 'Whatsapp', 'Amazon'}
s1 = {'Whatsapp','Snapchat','Instagram','Myntra'}
s2 = {'Amazon','Flipkart','Meesho','Zomato'}
print(s1.isdisjoint(s2))
print(s1.issubset(s0))
print(s0.issuperset(s2))