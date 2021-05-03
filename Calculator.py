# Given below is a python Calculator
''' Ok
Now Let's get started.
'''
print("Hi! So lets start with making a simple calculator.")

def geeks():
    print("Please select operation -\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n")

    select = int(input("Select operations form 1, 2, 3, 4 :")) # Take input from the user
    def add(num1, num2):  # Function to add two numbers
        return num1 + num2

    def subtract(num1, num2):  # Function to subtract two numbers
        return num1 - num2

    def multiply(num1, num2):  # Function to multiply two numbers
        return num1 * num2

    def divide(num1, num2):  # Function to divide two numbers
        return num1 / num2

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if select == 1:
        print(number_1, "+", number_2, "=",
                        add(number_1, number_2))

    elif select == 2:
        print(number_1, "-", number_2, "=",
                        subtract(number_1, number_2))

    elif select == 3:
        print(number_1, "*", number_2, "=",
                        multiply(number_1, number_2))

    elif select == 4:
        print(number_1, "/", number_2, "=",
                        divide(number_1, number_2))
    else:
        print("Invalid input")

def sand():
    print("kay let's start!")
    


calc = int(input("Type of Calculator: 1. Geeks for geeks 2. Sandeep's"))
if calc == 1:
    geeks()
elif calc == 2:
    sand()
