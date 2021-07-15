#loops - repetitive tasks

# for example, if you want to print something 10 times, you can use loops
# --> efficient way of doing it

#two kinds of loops: for loops and while loops
#for loops - if you know how many times to repeat
#while loops - don't know how many times to repeat

#FOR LOOPS: sequence, strings, lists, disctionaries

# a = [1,2,3,4]
# print(a[1:4])

# for number in range(10): #iterate through sequence of numbers, 0,1,2,3,...9
#     print(number)

# for num in range(5):
#     print(num)

# for num in range(1,11):
#     print(num)

# for num in range(1,11,2): #start, stop, step
#     print(num)

#USE FOR LOOP TO PRINT NUMBERS 0 TO 100 (inclusive)

# for number in range(101):
#     print(number)

# #USE FOR LOOP TO PRINT NUMBERS 0 TO 100 (skip 5),

# for number in range(0,100,5):
#     print(number)


# letters =  ["a", "b", "c", "d"]


# result = "" 
# for letter in letters:
#     result = result + letter
# print(result)

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# for item in range(len(chilli_wishlist)):
#     print(chilli_wishlist[item])

# for item in chilli_wishlist:
#     print(item)

# ADAPT THE FOR LOOP TO PRINT THE MESSAGE FOR EACH ITEM IN THE LIST E.G. "Chilli wants: item"

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# for item in chilli_wishlist:
#     print(f"Chilli wants: {item}")


# #USE FOR LOOP TO PRINT EACH ITEM IN A LIST FROM A PREVIOUS EXERCISE

# letters =  ["a", "b", "c", "d"]

# for letter in letters:
#     print([letter])


#NESTED LOOP

# numbers = [
#     [1,2,3],
#     [4],
#     [5,6]
# ]

# # print(numbers[2][1])

# for num in numbers: #every element in the main list
#     for digit in num: #every element in the sublist
#         print(digit)


# chilli_wishlist = [
#     ["igloo"],
#     ["donut toy", "tennis ball", "crocodile toy"],
#     ["chicken", "peanut butter"],
#     ["cardboard box", "kong", "dig mat"]
# ]

# for category in chilli_wishlist:
#     for item in category:
#         print(item)

