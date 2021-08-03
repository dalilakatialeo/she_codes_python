#Lists

# store multiple value in a single variable
# can be any data type
# they are mutable - we can change them


fruits = ["banana", "apple", "cherry"]
#lists use 0 base indexing

print(fruits[0]) #first element
print(fruits[-1]) # negative indexing - print the last

#append is a function to add a new list item
fruits.append("pineapple")
print(fruits)

#pop is a function to delete a list item - deletes the last one by default, unless index is specified
fruits.pop()
print(fruits)

digits = [1, 2, 3]
decimals = [1.12, 12.4]
nested_list = [[1,2,3],["hello"]] #list of lists

#loop through a list with a for loop

for item in fruits: #item is a variable, can be anything, but best if it makes sense
    print(item)

#loop through a nested list

for item in nested_list:
    print(item)  #prints the sublists
    #printing is a great debugging tool - helps you understand what is going on
    #this is outputting lists. we can loop through again to extract the elements
    for i in item: #i is a variable within item
        print(i) #prints the items inside the sublist

people = [
    ["Alice", 25, "pink"],
    ["Bob", 33, "purple"],
    ["Ann", 18, "red"]
]

vaccination = []

for person in people:
    print(person) #this prints the whole sublists
    #while we loop through we gain access to all data

# # Pseudo code - rather than writing code and syntax, we can put our logic into english statements
# # Build the logic without writing any code - it reinforces your logic and creates a plan
# # Problem solving
# # go through the list
# # check age
# # if age is 20 or older, add this person to a list

# for person in people:
#     if person[1] >= 20: #["Alice", 25, "pink"], ["Bob", 33, "purple"], ["Ann", 18, "red"]
#         vaccination.append(person[0]) # we want to add that person's NAME 
# print(vaccination)

# # it is always good to print out and see where we are!


# grid = [
#     ['X', 'O', 'X', 'O'],
#     ['X', 'X', 'O', 'O'],
#     ['X', 'X', 'X', 'O'],
#     ['X', 'X', 'O', 'O']
# ]

# # x_count = 0 #in python we need to assign a variable to a value. Always good to create a variable when we want to track something

# # create a for loop for each row
# #create another for loop to check each item
# #check if the item is X
# #create a count X which is zero and if it is an x
# # increment the counter

# for row in grid:
#     x_count = 0
#     # print(row)
#     for char in row:
#         if char == 'X':
#             x_count += 1
#     print(x_count)


#Dicitonaries
phone = {"Asli":12, "Bel":13, "Asli":10} #key and value pair #keys are unique, if named more than once, latest value is stored
print(phone["Asli"]) 
phone["Kate"] = 60
print(phone)

#for loops for lists
# for person in phone:

#for loops in dictionaries - we can use the items fucntions

for name, number in phone.items(): #
    print(type(number))
