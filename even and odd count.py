""" using while loop
num=int(input("Enter Number :"))
oddno=0
evenno=0
while round(num/10)!=0:
    mod=num%10
    print(num)
    if(mod%2==0):
        evenno+=1
    else:
        oddno+=1
    num=round(num/10)
    if(round(num/10)==0):
         if(num%2==0):
            evenno+=1
         elif(num%2!=0):
             oddno+=1

print(f"Count of even no is:{evenno}")
print(f"Count of odd no is:{oddno}")

"""

#using Do while loop

num=int(input("Enter Number :"))
oddno=0
evenno=0
while (True):
    if(num!=0):
        mod=num%10
        print(num)
        if(mod%2==0):
            evenno+=1
        else:
            oddno+=1
        num=int(num/10)
    else:
        break
        
print(f"Count of even no is:{evenno}")
print(f"Count of odd no is:{oddno}")

"""
num = int(input("Enter Number: "))
oddno = 0
evenno = 0

while num > 0:
    mod = num % 10
    
    if mod % 2 == 0:
        evenno += 1
    else:
        oddno += 1
    num //= 10
    print(num)


print(f"Count of even digits: {evenno}")
print(f"Count of odd digits: {oddno}")"""

"""sum=78 // 10
s=int(78/10)
print(sum)
print(s)"""