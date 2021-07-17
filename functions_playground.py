
# #create a function


# def ask_name():  #def is a keyword to define a function, brackets tell the program that it's a fucntion.
#     name = input("What's your name? ") #create a variable - this is called a local variable beause it is accessed locally
#     return name #this is the halting point for the program
#     print("hello") #the colour fades - it means it's unreachable and wont be performed!

# # ask_name() # this function returns a string

# #we need to make use of the data we are grabbing, so we need to store it into a variable

# asli_name = ask_name() #we will call the function

# print(asli_name)

# def create_greeting(name): #name could be anything. Needs to be semantic so it can easiy be referenced.
#     greeting = f"Hello {name}"
#     return greeting
# print(create_greeting("Chilli"))
# print(create_greeting("Angela"))


#CHALLENGE - create a funciton that takes in an integer as a parameter and returns that integer multiplied by 3

# def multiply(number):
#     return (int(number) * 3)

# print(multiply(3))

# def convert_cm_to_inch(length_cm):
#     length_inch = length_cm / 2.54
#     return length_inch
# print(convert_cm_to_inch(20))

# length_inch  #is not defined outside of the funciton, can only be accessed from within the function

#CHALLENGE - write a function that converts inches to cm

# def convert_inch_to_cm(length_inch):
#     length_cm = length_inch * 2.54
#     return length_cm
# print(convert_inch_to_cm(7.8))

# def add(a,b): #parameters can be anything. function will add the two parameters and return the result
#     return a+b #a fucntion doesnt need to return aything

# print(add(2,3))

def calculate_mean(a, b):
    total = a + b
    mean = total / 2
    return mean

print(calculate_mean(3,4))
