# VARIABLE ARGUMENT IN PYTHON


# def add(*anyName):
def add(*args):
    print(args)
    print(type(args))

    sum =0
    for i in args :
        sum += i


add(10,20,30,40)
add(50,4,66,80)
""" thus variable argument will store value in form of tupple"""

def addAgain(numbers):
    sum = 0
    for data in numbers:
        sum = sum + data

    print(">> sum is:", sum)


data = (10, 20, 30, 40, 50)
addAgain(data)