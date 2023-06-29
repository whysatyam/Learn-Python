try:
    number = int(input("enter a number: "))
    print(number)

except ZeroDivisionError:
    print("divided by zero")     # it will show up if we enter a value like this 10/0 , 29/0 etc
except ValueError:
    print("invalid input")       # it will show up if we enter a string rather than a number






