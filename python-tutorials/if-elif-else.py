x = 300
y = 300
z = 300

if x>y and x>z:
    print(f'{x} is largest')

elif y>x and y>z:
    print(f'{y} is largest')

elif z>x and z>y:
    print(f'{z} is largest')

else:
    print('NUMBERS ARE EQUAL')