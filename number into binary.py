num=18
q=0
binary=""

while round(num%10)!=0:
   q=num%2
   binary=str(q)+binary
   num=int(num/2)
print(binary)