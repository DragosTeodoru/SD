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
#a) "then" is not part of the "if" statement
#b) x/y not defined
#c) y not defined
#d)
letterGrade= "F"



#Task 12

print()
#Task 13
print("1x    2x    3x")
print("--------------")
for i in range(1,6):
    print(i,"   ",i**2,"    ",i**3)
