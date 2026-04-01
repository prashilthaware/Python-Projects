
incompltetask=[]
compltetask=[]
option=0

def addtask():
    task=input("Add task:")
    print("Task added successfully.")
    incompltetask.append(task)
    
    

def taskcomplte():
    print("Incomplte Task list.")

    for i in range(1,len(incompltetask)+1):
        print(i,".",incompltetask[i-1]) 

    opt=int(input("Enter option to complte task:"))
    compltetask.append(incompltetask[opt-1])
    incompltetask.pop(opt-1)
    print("Task complte succesfully.")
    
    
def complettask():
    print("Completed task list:")
    i=0
    for tasklist in compltetask:
        i+=1
        print(i,".",tasklist)
    print("_____________________")



while option !=4:
    print("1. Add Task.")
    print("2. Mark task as complted task.")
    print("3. View complted task.")
    print("4. Exit")

    option=int(input("Enter Option:"))

    match (option):
        case 1:
            addtask()
        
        case 2:
            taskcomplte()
        
        case 3:
            complettask()
        
        case 4:
            print("Exit!!!")
