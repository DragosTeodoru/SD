#Task 1
n=0
pi=0
while  n<10000000:
    pi+=(-1)**n*4/(2*n+1)
    n+=1
print(pi)

#Task 2

a=[66.25, 333, 333, 1, 1234.5]
print(a)
a.insert(2, -1)
print(a)
a.append (333)
print(a)
a.index(333)
print(a)
a.remove(333)
print(a)

#Task 3
x=0
squares=[]
for x in range(0,11):
    squares.append(x*x)
print(squares)

#Task 4 Every group possible of every 2 items from both lists
nums=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            nums.append((x,y))
print(nums)
# Task 5
print("Add items to your shopping list.")
Shoppinglist=[]
item=input
while item!="":
    item=input("Add item to the list: ")
    if item==input:
        break
    elif item!="":
        Shoppinglist.append(item)
        print(item + " has been added to the shoping list!") 
print ("Here's your shoping list: "+str(Shoppinglist))

#Task 6
a = []
sentence1=input("enter the first sentance: ")
sentence2=input("enter the second sentance: ")

#a
print(sentence1+ " " +sentence2)
a.append((sentence1+ " " +sentence2))
#b
a=sentence1.split() + sentence2.split()
print(a)
#c
a.sort()
print(a)
#d
print(len(a))
#e
def word_count(value):
    count = dict()
    sentence = value
    for word in sentence:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
print(word_count(a))
#f
    
for i, word_count in enumerate(a,1):
    print("[%d]: %s"% (i,word_count))

