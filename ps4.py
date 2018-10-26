#Task 1
radius=int(input("Radius:"))
x=3.14
pi=x
area=pi*radius**2
print (area)

#Task 2
x=4
y=5
a=3*(x+y)
print (a)

#Task 3
radius=float(input("Enter the radius:"))

#Task 4
print((3+4+5)/3)

#Task 5
x=19.93
y=20.00
z=y-x
print("%.2f" %z)

#Task 6
x=2
print("x, squared is, x*x")
xcubed=x**3
print (xcubed)

#Task 7
from math import sqrt
x=2
y=4
print("The product of ", x, "and", y, " is ", x * y)
print("The root of their difference is ", sqrt(abs(x - y)))

#Task 8
name=input("Enter your name: ")
age=int(input("Enter your age: "))
age=age+1
print ("Hello " + name +", next year you will be " + str(age) +" years old!")

#Task 9
radius= ("Radius is: %6.d" %2)
area=("Area is: %8.2f" %12.5678)
print (radius)
print (area)
#Task 10
p=17
q=18

print(p//10+p%10)
print(p%2+q% 2)
print((p+q)//2)
print((p+q)/2.0)
