#calculator
import artcalculator
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print(artcalculator.logo)
#let's create a dictinary with keys as symbols and functions

symbols={"+":add,"-":subtract,"*":multiply,"/":divide}
validate=True
def calculator():
    first=int(input("enter the number:"))
    for i in symbols:
        print(i)
    while validate:
        operator=input("select a operator:")
        second=int(input("enter the other number"))
        cal_operator=symbols[operator]
        result=cal_operator(first,second)
        print(f"{first} {operator} {second} = {result}")
        if (input("enter 'y' to continue and 'n' start a new calculation "))=="y":
            first=result
        else:
            validate=False
            calculator()
