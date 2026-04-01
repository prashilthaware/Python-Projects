
def depositmoney(bal):
    dmoney=int(input("Enter money to deposit:"))
    mstate.append(f"+{dmoney}")
    bal+=dmoney
    print(f"Your Current balance is {bal}")
    return bal

def withdrawmoney(fbal):
    wmoney=int(input("Enter money to withdraw:"))
    if(fbal>=wmoney): 
        fbal-=wmoney
        print(f"Your Current balance is {fbal}")
        mstate.append(f"-{wmoney}")
    else:
        print("Enter amout is greater")
    return fbal

def ministatement():
    print(mstate)

def pinchange():
    newpin=int(input("Enter New Pin:"))
    pin=newpin
    print(f"Your New pin is {pin}")
    return newpin

def checkbalance(bal):
    print(f"Your Balance is {bal}")

def checkpin():
    userpin=int(input("Enter pin:"))
    if(userpin==pin):
        return True
    else:
        print("Invaild pin!!!")
        return False


balance=int(input("Enter Balance:"))
mstate=[]
pin=123

option=0


while option!=6:
    print("1. Deposit money.")
    print("2. Withdraw money.")
    print("3. Mini Statement.") 
    print("4. Change Pin.")
    print("5. Check Balance.")
    print("6. Exit")


    option=int(input("Enter Option:"))

    match(option):
        case 1:
            if(checkpin()==True):
                balance=depositmoney(balance)
        
        case 2:
            if(checkpin()==True):
                balance=withdrawmoney(balance)
    
        case 3:
            if(checkpin()==True):
                ministatement()
    
        case 4:
            if(checkpin()==True):
                pin=pinchange()

        case 5:
            if(checkpin()==True):
                checkbalance(balance)
        
        case 6:
            print("Exit!!!!")