# is_raining = False
# is_cold = True

# print(is_raining)
# # print(type(is_raining))
# # print(is_cold)
# # print(type(is_cold))

# print (not is_raining)
# print(is_raining and is_cold)
# print(is_raining and not is_cold)

# print(is_raining) #F
# print(not is_raining) #T
# print(is_raining or is_cold) #T
# print(is_raining and not is_cold) #F
# # print(is_raining or not is_cold) #F
# # print(not is_raining and not is_cold) #F

# temperature = 16
# print(temperature < 18)
# wind_chill = 3
# print (wind_chill > 4)
# print(temperature - wind_chill < 16)

# # name = "Hayley"
# # print(name == "Hayley")
# # print(name != "Hayley")


# print("A" > "a") #checking ASCII table values! #F
# print("a" > "A") #checking ASCII table values! #T
# print(ord("A")) #checks the ASCII value


###########################################
# IF STATEMENTS
# syntax / semantics
# syntax is the grammar - need to follow rules
# semantics are the logic of the program

# name = "Randall"

# if name == "Asli":
#     # after the colon we have the body. 
#     print("Hello Asli")
# elif name == "Randall":
#     print("Hi Randall")
# else:
#     print("Hello")

# is_raining = False

#if

# if is_raining:
#     print("Take an umbrella.")

#if and else

# if is_raining:
#     print("Take and umbrella.")
# else:
#     print("Do not take an umbrella.")

#if, elif and else
temperature = 16
wind_chill = 3
is_raining = False
# if temperature - wind_chill < 16:
#     print("Take a jumper.")
# elif temperature - wind_chill > 30:
#     print("Euck, it's hot today, stay home.")
# else:
#     print("Wow, what lovely day")

#nested if statements

if temperature - wind_chill < 16 and is_raining:
    print("Just stay home.")
else:
    if is_raining:
        print("You'll need an umbrella today.")
    if temperature - wind_chill < 16:
        print("You'll need a jumper today.")