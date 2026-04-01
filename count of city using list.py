"""count=0
cities=["amravati","amravati","nagpur","washim","buldhana","akola","akola","nagpur",]
usercity=input("Enter City:")

for city in cities:
    if(city==usercity):
        count+=1    
if (count==0):
    print("City is not found")
else:
    print(usercity," : ",count)

"""

cities=["amravati","amravati","nagpur","washim","buldhana","akola","akola","nagpur","amravati"]

for city in cities:
    count=0
    for cmpcity in cities:
        if cmpcity==city:
            count+=1
    print(city,":",count)