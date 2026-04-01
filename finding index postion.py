lnum=[1,2,3,6]
print(lnum)
position=0
num=int(input("Enter number in the above number:"))

for n in lnum:
    if num==n:
        print(lnum.index(n))
    