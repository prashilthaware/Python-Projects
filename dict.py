student={"Name: ":"Prashil","Age: ":19,
         "Collage: ":"Takshshila Polytechnic",
         "Address: ":"Amravati","Year: ":"3rd",
         "Branch: ":"Compyter Engg"}

student["Roll no: "]= 65 #for Adding new key , value in dict  

student.pop("Age: ") #for remove key , value.
#print(student)
#print(student["Name"]) #for print single key , value.
studentinfo=student.items() # store dict element in vriable

for k,v in studentinfo: #loop operation in dict
    print(k,v)