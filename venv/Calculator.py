def add():
    a = int(input("Enter a number. "))
    b = int(input("Enter another number. "))
    print("The sum of two numbers are :", a+b)


def substraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)


def multiplication():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a * b)


def division():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a / b)


operation = input("Please type +, -, * or / ")

if operation == '+':
    add()
elif operation == '-':
    substraction()
elif operation == '*':
    multiplication()
else:
    division()


