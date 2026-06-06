try:
    age = int(input("Enter your age: "))

    if age > 0 and age <= 120:
        if age % 2 == 0:
            print("Valid age. Age is even.")
        else:
            print("Valid age. Age is odd.")
    else:
        print("Invalid age entered.")

except ValueError:
    print("Invalid input. Please enter a number.")