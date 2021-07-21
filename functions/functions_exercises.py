# def convert_inch_to_cm(length_inch):
#     length_cm = length_inch * 2.54
#     return length_cm
# print(convert_inch_to_cm(7.8))


######Q1 - Write a function that takes a temperature in fahrenheit and returns the temperature in celsius

# def fahr_to_c (temp_f):
#     temp_c = (temp_f -32)* (5/9)
#     return temp_c
# print(fahr_to_c(350))


#######Q2 - Write a function that accepts one parameter (an integer) and returns True when that parameter is odd and False when that parameter is even

# def odd_number(number):
#     if (number % 2) == 0:
#         return False
#     else:
#         return True
# print(odd_number(-1))


######Q3 - Write a function that returns the mean of a list of numbers

# def list_mean(list):
#     return sum(list) / len(list)
# print(list_mean([10,5,6]))


#######Q4 - Write a function that takes two parameters: the unit price of an item and how many units were purchased. Return the total cost as a string.

def purchase(price, qty):
    return price * qty
print(f"${purchase(1.49, 7):.2f}")