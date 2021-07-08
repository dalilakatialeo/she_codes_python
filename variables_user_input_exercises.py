# Q1
# take two numbers from user, output their sum

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# user input is always a string. Need to type parse.
# we type parse to float, because the expected result as per example is a float.
# be mindful of syntax and parenthesis!
print(float(num1) + float(num2))


# Q2
#take two numbers from user, output the multiplication equation!

num3 = input("Enter a number: ")
num4 = input("Enter another number: ")

# Input is always a string. Need to type parse to perform operations.
# Type parse to float because this is what the example shows
input1 = float(num3)
input2 = float(num4)

# Create a new variable for the multiplication result.
multiply = input1 * input2

# formatting into a string
print(f"{input1} * {input2} = {multiply}")


# Q3

km = input("How many kilometres? ")

# input is always a string.
# create new variables with new value and type parse to float so we can cover any input quantity

meters = float(km) * 1000
centimeters = float(km) * 100000

# format as string and type parse to int so we don't have float as results.

print(f"{km}km = {int(meters)}m")
print(f"{km}km = {int(centimeters)}cm")


# Q4

name = input("What is your name? ")
height = input("How tall are you (cms)? ")

print(f"{name} is {height}cms tall.")