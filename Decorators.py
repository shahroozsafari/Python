import time 

  
#--------Calculate Time Decorator--------
def calculate_time(func):
    
    def wrapper(a): 
        print("----------------------")
        begin = time.time() 
        print(func(a))
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin) 
        print("----------------------")
        return func(a)
    return wrapper
#----------------------------------------
@calculate_time
def factorial(num): 
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
#----------------------------------------

#-------Login Decorator------------------
def login(func):
    User_Pass={"Ali":"123","Reza":"124","Payam":"125"}
    def checker():
        User=input("Enter User Name : ")
        Pass=input("Enter Password : ")
        for check in User_Pass.items():
            if (User,Pass)==check:
                func()
                return func
            
        print("User and/or Password is not Valid !")
        exit()

    return checker
#----------------------------------------
@login
def report1():
    print("---------REPORT--------")

#----------Main--------------------------
factorial(80)
report1()
