groceries = [
    ["Baby Spinach ", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers     ", 2.10],
    ["Bacon        ", 9.00],
    ["Carrots      ", 0.56],
    ["Oranges      ", 3.08]
]

# total_receipt = 0.00
total = 0.00

for item in groceries:
    enter_qty= input("How many units?")
    multiply = item[1] * int(enter_qty)
    total = total + multiply

print(f"====Izzy's Food Emporium====")
for item in groceries:

    print(f"{item [0]}       ${multiply}")
print(f"=============================")
print(f"                   ${total}")



#why is price wrong?