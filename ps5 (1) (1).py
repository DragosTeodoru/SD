#Task 1
a=13
b=14
if (a+1)<=b:
    print("(a+1)<=b is true")
elif a+1>=b:
    print("a+1>=b is true")
elif a+1!=b:
    print ("a+1!=b is true")

#Task 2
myage=str(input("How old are you? "))
print("Hi there, you are " + myage +" old.")

#Task 3
number1	=int(input("Enter first number "))
number2	= int(input("Enter second number "))
result=str(number1 + number2)
print("The result is "+result)

#Task 4
print((3+11+78+112+4+18)/6)

#Task 5 
number=int(input("enter an integer number: "))
print("remainder " + str(number%7))
#Task 6
number//=7
if number ==1:
    print("the number fits " + str(number) +" time")
else:
    print("the number fits " + str(number) +" times")
#Task 7
 #not defined scoreA and scoreB

#Task 8
userInput=str(input("Enter Y to quit. "))
if userInput == ("y"):
    print("Goodbye")

#Task 9
#a) "then" is not part of the "if" statement and x have to be defined
'''x=4
if x>0:
    print (x)'''
#b) x/y not defined / import math / no output
import math
x=5
y=3
if 1+x>x**math.sqrt(2):
    y=y+x
#c) x and y not defined / no output
x=1
y=5
if x=1:
    y+=1
#d) "grade" not defined / no output
grade=59
letterGrade= "F"
if grade>=90:
    letterGrade="A"
elif grade>=80:
    letterGrade="B"
elif grade>=70:
    letterGrade="C"
elif grade>=60:
    letterGrade="D"

print( letterGrade)

#Task 10
richter= float(input( "Enter a magnitude on Richter scale number: "))
if  richter>=(8.0):
    print("Most structures fall")
elif richter>=(7.0):
    print("Many structures destroyed")
elif richter>=(6.5):
    print("Many buildings considerably damaged, some collapse")
elif richter>=(4.5):
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")

#Task 11
count=0
password=input("Please, enter your password: ")
while password!="changeme":
    if password==("changeme"):
         print("Accepted")
    elif password!=("changeme")and count<4:
        password=input("Password incorrect, try again...")
        count+=1
    else:
        input("Access denied, please press enter to exit and contact security to reset your password")
        break

#Task 12   coment
'''for i in range(3):
    for j in range (1,4):
        print (i+j, end="")
print ()'''
    


print()
#Task 13
print("x**1   x**2   x**3")
print("--------------------")
for i in range(1,6):
    print(i,"   ",i**2,"     ",i**3)
