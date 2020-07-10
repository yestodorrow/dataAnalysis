def printme(name="nobody",age=1):
    print("my name is "+name)
    print(age)

printme("liugang")

def ChangeInt(a):
    a=10

b=2
ChangeInt(b)
print(b)


mylist=[10,20,30]

def changeme(mylist):
    mylist.append([1,2,3,4])
    print(mylist)
    return;


# changeme(mylist)

def changeme2(mylist):
    newList=mylist
    newList.append([1,2,3,4])
    print(mylist)

changeme2(mylist)

total=0

def sum(arg1,arg2):
    global total
    total=arg1+arg2
    print(total)
    return total

sum(1,2)
print(total)

import math
print(math.pow(2,3))
print(dir(math))
print(math.sin(math.pi/6))

from math import sin 
print(sin(math.pi/6))


import sys
print(dir(sys))
print(sys.path)


