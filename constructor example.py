
class Employee:
    def __init__(self,name,id,address):
        print("constructor called")
        self.name=name
        self.id=id
        self.address=address

    def setaddress(self,salary):
        self.__salary=salary #private variable

    def getaddress(self):
        print("salary: ",self.__salary)
    
e=Employee("prasil",2006,"amravati")
print("name: ",e.name)
print("id: ",e.id)
print("address: ",e.address)
e.setaddress(500)
e.getaddress()