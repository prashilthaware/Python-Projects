s=int(input("Enter Starting Point:"))
e=int(input("Enter Ending Point:"))
add=0
for i in range(s,e+1,1):
    a=i%2
    if(a==0):
        add=add+i
print(add)





