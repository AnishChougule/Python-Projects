def num():
    number= int(input("Number? "))
    return number

def sqr():
    x=num()
    return x*x

def cube():
    x=num()
    return x*x*x

def sqrt():
    x=num()
    return x**0.5

def ifprime():
    x=num()
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                return False
            break
        else:
                return True
    else:
        return False

def primefactors():
    x=num()
    for i in range(1,x+1):
        if (x % i)==0:
            flag=0
            for j in range(2,i):
                if (i % j)==0:
                    flag=1
            if flag==0:
                print(i,end=" ")


def facto():
    x=num()
    fact = 1
    for x in range(1,x+1):
        fact=fact * x
    return fact

Operation={1:sqr,2:cube,3:sqrt,4:ifprime,5:primefactors,6:facto}

print('''1: Square
2: Cube
3: Square Root
4: Check if Prime
5: Prime Factors
6: Factorials''')

get_operation=int(input("Operation? "))

def error():
    print("Wrong Operation!")

output = Operation.get(get_operation,error)()

print("Result: ",output)