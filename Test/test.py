operation = input("Please pick an operation \n 1) Addition \n 2) Subtraction \n 3) Multiplication \n 4) Division: " )

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

def add(num1, num2):
    print (num1+num2)
    
    return (num1+num2)


def subtract(num1,num2):
    print (num1-num2)
    
    return (num1-num2)

def multiply(num1,num2):
    print (num1*num2)

    return (num1*num2)

def divide(num1,num2):
    print (num1/num2)

    return (num1/num2)

try:

    if operation == "1":
        result = add(num1,num2)
        print (result)

    elif operation == "2":
        result =  subtract(num1,num2)
        print (result)

    elif operation == "3":
        result =  multiply(num1,num2)
        print (result)

    elif operation == "4":
        result =  divide(num1,num2)
        print (result)

    else:
        print ("Invalid choice")

except ZeroDivisionError:
    print ("Error Division by 0 is not allowed")

except ValueError:
    print ("Please enter a vaild number")