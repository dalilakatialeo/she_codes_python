
#WHILE LOOPS - best used when we don't know how many times to repeat

# count = 0

# while count < 5: #while is a boolean operator
#     print("hello")  # keeps going, because its always true! infinite loop
#     # count = count + 1 #stops infinite loop!
#     count +=1 # it keeps adding 1 to the result #same as above

# guess = ""

# while guess != "a":
#     guess = input("Guess a letter: ")


# counter = 10

# while counter <= 10:
#     print(counter)
#     counter = counter +1

#CHALLENGE - ASK THE USER TO CONTINUALLY ENTER NAMES UNTIL A BLANK STRING IS ENTERED

name = "x"

while name != "":
    name = input("Please enter name: ")


#CHALLENGE - ASK THE USER TO CONTINUALLY ENTER A PASSWORD UNTIL A PASSWORD THAT YOU SET HAS BEEN GIVEN

password = ""

while password != "blueberry":
    password= input("Guess my password: ")

