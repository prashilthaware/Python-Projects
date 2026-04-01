s1=int(input("Enter the lenght of Side:"))
s2=int(input("Enter the lenght of Side:"))
s3=int(input("Enter the lenght of Side:"))

if(s1==s2 and s2==s3 and s1==s3):
    print("Triangle is equliateral")
elif(s1==s3 or s2==s3 or s1==s2):
    print("Triangle is isoscales")
else:
    print("Triangle is scalen")
