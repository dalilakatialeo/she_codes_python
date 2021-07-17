string = input("Please enter a string: ")

# print(string)

char_list=list(string)

# print(char_list)

for char in char_list:
    print(f"{char_list.index(char)} {char}")

    #if there is a double letter, it shares the same index?