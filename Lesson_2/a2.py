# 1) Start a `try` block to run code that may cause exceptions.
try:
# 2) Take two numbers from the user in a single input, separated by a comma:
#    a) Use `eval(input(...))` to read and convert the input.
#    b) Store the two values in `num1` and `num2`.
    num1 ,num2 = eval(input("Enter 2 numbers separated by a comma: "))
# 3) Perform division:
#    a) Compute `result = num1 / num2`.
#    b) Print the result.
    result = num1 / num2
    print (result)
# 4) Handle possible errors using multiple `except` blocks:
except ZeroDivisionError:
    print("Division by zero is error !!")
# 5) If a `ZeroDivisionError` occurs (when `num2` is 0),
#    print "Division by zero is error !!".

# 6) If a `SyntaxError` occurs (for example, the comma is missing or format is incorrect),
#    print a message explaining the correct input format: "1, 2".
except SyntaxError:
    print ("Re-enter 2 numbers SEPERATED by a COMMA\n Ex: 1, 2")
# 7) If any other error occurs, use a general `except` block
#    and print "Wrong input".
except:
    print ("Wrong input")
# 8) If no exception occurs in the `try` block, run the `else` block
#    and print "No exceptions".
else:
    print ("No exceptions")
# 9) Run the `finally` block no matter what happens (error or no error),
#    and print "This will execute no matter what".
finally:
    print ("This will execute no matter what")