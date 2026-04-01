import random
number=random.randint(1, 100)
while True:
    
    print(number)
    num=int(input("Enter a number: "))
    dis=abs(number-num)


    if number==num:
        print("Correct guess..")
        break
    elif number>num and dis>=10 :
        print("Too far")
    elif number<num or number>num and dis<=10:
        if dis>=10:
            print("Too far")
        else:
            print("Too close")


