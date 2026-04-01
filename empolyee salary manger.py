class Employee:
    
    def __init__(self,salary):
        salary=salary
        print(salary)
        self.initialsalary=salary
        print(f"Your initial salary is: {self.initialsalary}")
    
    def inscrisesalary(self, isalary,bonous):
        self.bonous=bonous
        salary=self.initialsalary
        #salary+=isalary
        if self.initialsalary <= salary and isalary+self.bonous*1.0<=self.initialsalary*0.1:
            self.initialsalary+=isalary
            self.initialsalary+=self.bonous
            if salary<=self.initialsalary:
                print(f"Your Inscise Salary is : {self.initialsalary}")
            else:
                print("Salary can not set")
        else: 
            print("Salary can not set")
        
e=Employee(100000)
e.inscrisesalary(5000,5000)
