class Person:
    personName = "Waseem"
    personCity = "Solapur"
    personBloodGroup = "O+"
    personId = 123456

    def setPerson(self):
        self.personName = input('ENTER PERSON NAME - ')
        self.personCity = input('ENTER PERSON CITY - ')
        self.personBloodGroup = input('ENTER PERSON BLOOD GROUP - ')
        self.personId = input('ENTER PERSON ID - ')

    def getPerson(self):
        print(f'PERSON NAME - {self.personName}')
        print(f'PERSON CITy - {self.personCity}')
        print(f'PERSON BLOOD GROUP - {self.personBloodGroup}')
        print(f'PERSON ID   - {self.personId}')

p1 = Person()
print(p1)
p2 = Person()
print(p2)

print(p1.personId)
print(p1.personName)
print(p1.personBloodGroup)
print(p1.personCity)

p2.personName='Sadik'
p2.personCity='Mumbai'
p2.personBloodGroup='A+'
p2.personId = 245698
print(p2.personId)
print(p2.personName)
print(p2.personBloodGroup)
print(p2.personCity)
print("__________________________________________")

p3 = Person()

p4 = Person()

people = [p1,p2,p3,p4]
for i in people:
    i.setPerson()

for i in people:
    i.getPerson()