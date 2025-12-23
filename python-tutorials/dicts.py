# Dicts are ordered, mutable collection of the data that never repeat any value.

mydict = {
    'rollno' : '101',
    'name':'Alex',
    'std':'10th',
    'div':'A',
    'marks' : 89.98
}
print(mydict)
print(type(mydict))
print(len(mydict))

demo = dict((('empId',1001),('empName','Sarah'),('empSalary',55000)))
print(demo)
print(demo['empId'])
print(demo['empName'])
print(demo['empSalary'])
print("--------------------")

mydict.update({'city':'Solapur'})
print(mydict)

mydict.update({'state':'Maharashtra','country':'India','std':'5th'})
print(mydict)

mydict['mothertongue'] = 'English'
print(mydict)

mydict['div'] = 'D'
print(mydict)
print('-------------------------------------------')

mydict.popitem()
print(mydict)

mydict.pop('marks')
print(mydict)

del mydict['rollno']
print(mydict)

mydict.clear()
print(mydict)

# del mydict
# print(mydict)

for i in demo:
    print(i,demo[i])

for i in demo.values():
    print(i)

print("________________________")

id = int(input('ENTER PRODUCT ID - '))
name = input('ENTER PRODUCT NAME - ')
price = int(input('ENTER PRODUCT PRICE - '))
make = input('ENTER PRODUCT MAKE - ')

product = {
    'prodId':id,
    'prodName':name,
    'prodPrice':price,
    'prodMake':make,
}

print(product)