# Q1

groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
    }

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
    }


# for item in groceries: #item is the key
#     print(f"{quantity[item]} {item} @ ${groceries[item]} = {quantity[item] * groceries[item]:.2f}") 

# Q2

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
    }

colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green"
    ]

# for colour in colours:
#     colour_counts[colour] += 1

# print(colour_counts) #redo and format as per exercise output

#Q3

names = [
    "Maddy", 
    "Bel", 
    "Elnaz", 
    "Gia", 
    "Izzy",
    "Joy", 
    "Katie", 
    "Maddie", 
    "Tash", 
    "Nic",
    "Rachael", 
    "Bec", 
    "Bec", 
    "Tabitha", 
    "Teagen",
    "Viv", 
    "Anna", 
    "Catherine", 
    "Catherine", 
    "Debby",
    "Gab", 
    "Megan", 
    "Michelle", 
    "Nic", 
    "Roxy",
    "Samara", 
    "Sasha", 
    "Sophie", 
    "Teagen", 
    "Viv"
    ]

# names_dict = {}.fromkeys(names, 0)

# for name in names:
#     names_dict[name] += 1

# print(names_dict)

#Q4

import csv

colours_dict = {}

with open ("colours_20_simple.csv", mode = "r", encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next (csv_reader)
    for line in csv_reader:
        colours_dict[line[1]] = line[2] #key is going to be in line[1] and the value is going to be in line[2]
        #this is how we are creating key:value pair
print(colours_dict)

#Q5

colours_dict = {}

with open ("colours_20_simple.csv", mode = "r", encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next (csv_reader)
    for line in csv_reader:
        colours_dict[line[1]] = [line[0],line[2]] #value is a list. create an empty list with [], and populate it with two list items
print(colours_dict)