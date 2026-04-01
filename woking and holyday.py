day=input("Enter name of day:")

if(day=="mon" or day=="tue" or day=="wed" or day=="thus" or day=="fir"):
    print("Woking day")
elif(day=="sat" or day=="sun"):
    print("holyday")
else:
    print("enter valid day")