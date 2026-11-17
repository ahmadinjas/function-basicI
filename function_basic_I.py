

#1 

def a(): 
    return 5 

print(a()) 
#  I expected it to be printed : non 
#  but printed : 5 

#2  

def a() : 
    return 5 
print(a()+a())

#I expected it to be printed : 5 5
# but printed : 10

#3 

#3
def a():
    return 5
    return 10
print(a()) 

#I expected it to be printed : 15
#but printed : 5

#Because the first `return` statement a function executes causes it to stop immediately; any lines following it are not read.


#4  

#4
def a():
    return 5
    print(10)
print(a()) 

#I expected it to be printed : 10 ... 5 
# but printed : 5


#5
def a():
    print(5)
x = a()
print(x) 

#I expected it to be printed : 5 
#but printed : non
#Because there is no `return` in the function. 


#6 

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) 

#I expected it to be printed : non
#but printed : 3..5...erro
#Because there is no `return` in the function. 

#7  

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) 

#I expected it to be printed : 2 5
#printed : 2 5 

#8 

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#I expected it to be printed : 10
#but printed : 100...10


#9 

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#I expected it to be printed : 7/14/21
# printed : 7/14/21

#10 

def a(b,c):
    return b+c
    return 10
print(a(3,5)) 

#I expected it to be printed :8
#printed : 8


#11 

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b) 

#12 

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b) 


#11+12 

# I expected it to be printed : 500 \ non \ 500\500 
# but printed : 500\500\300\500


#13 

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b) 

#I expected it to be printed : 500/500/non/300
# but printed : 500/500/300/300


#14 
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() 

#I expected it to be printed : 1
# but printed : 1\3\2 

#15 

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y) 

# I expected it to be printed : 1/ 3 
# but printed : 1/3/5/10
 