number = input("Enter a number: ")

row = "*"
print(f"Pyramid size: {int(number)}")
if number !=0:
        for n in range(int(number)):
            print(row)
            row = row + "*"
else:
    print("")
