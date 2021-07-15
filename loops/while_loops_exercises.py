# ####Q1

# number = input("Enter a number: ")
# total = 0

# while number != "":
#     total = total + int(number)
#     number = input("Enter a number: ")
# print(total)


# name = "x"

# while name != "":
#     name = input("Please enter name: ")



####Q2 - Used a For loop?
# How to use a while loop?

#USE FOR LOOP TO PRINT NUMBERS 0 TO 100 (inclusive)

# for number in range(101):
#     print(number)

# #USE FOR LOOP TO PRINT NUMBERS 0 TO 100 (skip 5),

# for number in range(0,100,5):
#     print(number)


# number = input("Enter a number: ")

# for number in range(1, int(number) +1, 2):
#     print(number)

####Q3

number = "25"
guess = input("Guess the number: ")


while int(guess) != int(number):
    if int(guess) < int(number):
        print("Too low!")
        guess = input("Guess the number: ")
    else:
        print("Too high!")
        guess = input("Guess the number: ")
print("Correct!")