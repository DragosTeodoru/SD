#Task 1 comment
def mystery(x, y):
    result = (x + y) / (y - x)
    return result

print(mystery(2,3))
#Task 2 comment
def main():
    a = 5
    b = 7
    print(mystery(a, b))
def mystery(x, y):
    z = x + y
    z = z / 2.0
    return z
main()
#Task 3 comment
def main():
    a = 4
    print(mystery(a + 1))
def mystery(x):
y = x * x
return y
main()
#Task 4
def isEven(i):
    return i % 2 == 0

for page in range(1,10):
    if isEven(page):
        print(page)
    else:
        print("%60s%d" % (" ", page))
#Task 5!!!!!!!!!!!!
def main():
    spaces = 0
    userInput=input("Enter sentence to calculate number of spaces between the words: ")
    for char in userInput :
        if char == " ":
            spaces = spaces + 1
    return spaces
print(main())

main()
#Task 6
def mystery(n):
    if n <= 0:
        return 0
    else:
        return n + mystery(n - 1)
print(mystery(4))
      
#Task 7
def mystery(n):
    if n <= 0:
        return 0
    else:
        return mystery(n // 2) + 1

print (mystery(20))
#Task 8
def f(x):
    return g(x) + math.sqrt(h(x))
def g(x):
    return 4 * h(x)
def h(x):
    return x * x + k(x) - 1
def k(x):
    return 2 * (x + 1)
#Task 9
def f(a): 
    if a < 0: 
        return -1 
    n = a 
    while n > 0: 
        if n % 2 == 0 : 
            n = n // 2 
        elif n == 1: 
            return 1 
        else: 
            n = 3 * n + 1 
    return 0 


