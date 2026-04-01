salary=int(input("Enter salary:"))

if(salary<=250000):
    print("No Tax")

elif(salary<=500000):
    val=salary/100*5
    print(f"{val} is tax")

elif(salary<=1000000):
    val=salary/100*20
    print(f"{val} is tax")

elif(salary>=1000000):
    val2=salary/100*30
    print(f"{val2} is tax")
