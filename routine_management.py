
print("*****ROUTINE MANAGEMENT********\n ")   
def getdate(): 
    import datetime
    return datetime.datetime.now()
def log(i):
    if i==1 : 
        print("enter 1 for food and 2 for exercises") 
        a = int(input("")) 
        if a==1 :
            print("enter the food you wanted to add") 
            with open("harry_food.txt","a") as f:
                f.write(input("") +"\n") 
                f.write(str(getdate()))
        if a==2 :
            print("enter the exercise you wanted to add") 
            with open("harry_exercise.txt","a") as f:
                f.write(input("")+"\n")     
                f.write(str(getdate()))
    if i==2 :
        print("enter 1 for food and 2 for exercises") 
        a = int(input("")) 
        if a==1 :
            print("enter the food you wanted to add") 
            with open("manan_food.txt","a") as f:
                f.write(input("")+"\n")
                f.write(str(getdate()))
        if a==2 :
            print("enter the exercise you wanted to add") 
            with open("manan_exercise.txt","a") as f:
                f.write(input("")+"\n")
                f.write(str(getdate())) 
    if i==3 : 
        print("enter 1 for food and 2 for exercises") 
        a = int(input("")) 
        if a==1 :
            print("enter the food you wanted to add") 
            with open("mosh_food.txt","a") as f:
                f.write(input("")+"\n")
                f.write(str(getdate()))
        if a==2:
            print("enter the food you wanted to add") 
            with open("mosh_exercise.txt","a") as f:
                f.write(input("")+"\n")
                f.write(str(getdate())) 
                
def retrive(i): 
    if i==1 : 
        print("enter 1 for food and 2 for exercises") 
        a = int(input("")) 
        if a==1 :
            print("enter the food you wanted to add") 
            with open("harry_food.txt") as f: 
                print(f.read())
                
        if a==2 :
            print("enter the exercise you wanted to add") 
            with open("harry_exercise.txt") as f:
                print(f.read()) 
    if i==2 : 
        print("enter 1 for food and 2 for exercises") 
        a = int(input("")) 
        if a==1 :
            print("enter the food you wanted to add") 
            with open("harry_food.txt") as f: 
                print(f.read())          
        if a==2 :
            print("enter the exercise you wanted to add") 
            with open("harry_exercise.txt") as f:
                print(f.read()) 
    if i==3 : 
        print("enter 1 for food and 2 for exercises") 
        a = int(input("")) 
        if a==1 :
            print("enter the food you wanted to add") 
            with open("harry_food.txt") as f: 
                print(f.read())       
        if a==2 :
            print("enter the exercise you wanted to add") 
            with open("harry_exercise.txt") as f:
                print(f.read()) 

print("Enter 1:harry 2:manan 3:mosh") 
k = int(input("")) 
print("Enter 1 to log and 2 to retrive") 
j= int(input("")) 
if j==1: 
    log(k)  
if j==2: 
    retrive(k)