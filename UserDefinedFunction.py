#Function with no argument & no return value.

def printline():
    print("*"*50)

printline()
print("Welcome To User Defined Function In Python.")
printline()

#Function with argument but no return value.

def add(a,b):
    print("Addition : ",a+b)

printline()
add(10,20)
printline()

#Function with argument & return value.

def sub(a,b):
    return a-b

printline()
ans=sub(10,20)
print("Subtraction : ",ans)
printline()
