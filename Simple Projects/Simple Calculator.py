def add():
    x,y=getnum()
    return x+y

def sub():
    x,y=getnum()
    return x-y

def div():
    x,y=getnum()
    return x//y

def multi():
    x,y=getnum()
    return x*y

def getnum():
    num1=int(input("Number 1: "))
    num2=int(input("Number 2: "))
    return (num1,num2)

operation={1:add,2:sub,3:div,4:multi}

print('''1. Add
2. Substract
3. Divide
4. Multiply''')

command= int(input("Operation? "))

def error():
    print("wrong Operation!")

output=operation.get(command,error)()

print("Result: ",output)