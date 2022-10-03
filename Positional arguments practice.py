def questions():
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number: "))
    addition(num1, num2)
    

def addition (num1, num2) :
    num3 = (num1 + num2)
    print (num3)
    

def dob():  
    dob = int(input("what year were you born?"))
    year = int(input(" what year was it again?"))
    print ("Oh , so you're " , year - dob , "years old")

questions()
addition()
