bal=5000
print(f"Your curent balance is {bal}")
w=int(input("Enter Amount to withdraw:"))

if(w<bal):

    n=w%100
    if(n==0):
        bal=bal-w
        print(f"your balance is {bal}")
    else:
        print("Enter the amout x100")

else:
    print("enter amount is greater than balance")