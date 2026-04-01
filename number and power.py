"""num=int(input("Enter Number: "))
power=int(input("Enter Power: "))

total=1
for i in range(1,power+1,1):
    total=num*total
print(total)"""

i=0
total=1
num=int(input("enter number:"))
power=int(input("Enter Power: "))

while power>i:
    total=num*total
    i+=1
print(total)
