s1=int(input("Enter the lenght of Side:"))
s2=int(input("Enter the lenght of Side:"))
s3=int(input("Enter the lenght of Side:"))

if(s1==s2):
    if(s2==s3):
        print("Triangle is equliateral")
    else:
        print("Triangle is isoscales")
elif(s1==s3):
    print("Triangle is isoscales")
elif(s2==s3):
    print("Triangle is isoscales")
else:
    print("Triangle is scales")
