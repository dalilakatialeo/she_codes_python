groceries = [
    ["Baby Spinach ", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers     ", 2.10],
    ["Bacon        ", 9.00],
    ["Carrots      ", 0.56],
    ["Oranges      ", 3.08]
]

total = 0.00

for item in groceries:
    qty = input("How many? ")
    item.append(int(qty))
    total = total + (item[1]*item[2])
    
# print(groceries)
# print (total)

print("====Izzy's Food Emporium====")

for item in groceries:
    print(f"{item[0]}           ${item[1]*item[2]}")
    
print(f"============================= \n                       ${total}")