num=int(input("Enter Number: "))
#num_str=str(num)
#num_len=(len(num_str))
#print(num_len)
#i=1
total=0
while round(num/10)!=0:
    mod_num=num%10
    total+=mod_num 
    num=round(num/10)
    if(round(num/10)==0):
        total+=num
print(total)


