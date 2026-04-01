totalamount=0
option=0
expens=[]

def addexpense():
    expenl={}
    itemname=input("Enter Name:")
    expenl["name"]=itemname
    itemamount=int(input("Enter amount:"))
    expenl["amount"]=itemamount
    itemcategory=input("Enter Category:")
    expenl["category"]=itemcategory
    expens.append(expenl)
    print("Expense Add Successfully...")
    return itemamount

def viewexpence():
    for ex in expens:
        print(ex)

def filtercategory():
    entercategory=input("Enter category for fiter:")
    for ex in expens:
        if  ex["category"]==entercategory:
            print(ex)
        


while(option<=5):
    print("1. Add Expense.")
    print("2. View Expenses.")
    print("3. View Total.")
    print("4. Filter by category.")
    print("5. Exit.")
    option=int(input("Enter option: "))

    match option:
        case 1:
            totalamount+=addexpense()
        case 2:
            viewexpence()
        case 3:
            print(f"Total amount is: {totalamount}")
        
        case 4:
            filtercategory()
        
        case 5:
            print("Exit!!!!!")
