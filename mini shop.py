print("1. Add Item")
print("2. Exit")

item={}
total=0

option=int(input("Enter Option: "))

while option!=2:
    if option==1:
        itemname=input("Enter Item Name:")
        itemprice=int(input("Enter Item Price:"))
        item[itemname]=itemprice
        total+=itemprice

    print("1. Add Item")
    print("2. Exit")
    option=int(input("Enter Option: "))


iteminfo=item.items()
for k,y in iteminfo:
    print(k,y)

taxvalue=total/100*18


print(f"Your Total Amount is :{total} + tax:{taxvalue} = {total+taxvalue}")