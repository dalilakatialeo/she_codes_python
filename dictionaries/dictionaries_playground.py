groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges" : 3.08
}
#key is a string because it needs to be immutable
print(groceries)
#prints with curly brackets etc because we are not looping

#look at a specific value
print(groceries["Baby Spinach"]) #can pass any other existing key
#if pass a key that doesnt exist, it will output error

#Add an item
groceries["Avocados"] = 1.00
# print(groceries)

#remove an item
del groceries["Bacon"]
print(groceries)

#iteration

for item in groceries:
    print(f"{item}: ${groceries[item]}")

#another way to iterate over a dictionary
for item, price in groceries.items(): #using the items function, takes both variables
    print(f"{item}: ${price}")

