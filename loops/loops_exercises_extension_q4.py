number = int(input("Pyramid size: "))

row = "*"

for n in range(number):
    print(f"{' ' * (number - (n+1))} {row}")
    row += 2 *"*"