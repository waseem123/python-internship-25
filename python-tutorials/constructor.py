class MobilePhone:
    brand = ""
    model=""
    price=0

    def __init__(self,brand,model,price):
        print("HELLLO")
        self.brand = brand
        self.model = model
        self.price = price

    def getPhone(self):
        print(self.brand,self.model,self.price)

p1 = MobilePhone('Samsung','S24 Ultra',124000)
p2 = MobilePhone('Nothing','Phone 1',40000)
p3 = MobilePhone('One Plus','11',25000)

p1.getPhone()
p2.getPhone()
p3.getPhone()
