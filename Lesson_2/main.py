try:
    number = int(input("Enter the number: "))
    print (number)
except ValueError as ex: 
    print ("Execption",ex)