a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

# list1 = [
#     a,
#     b,
#     c
# ]
# print(list1)

list2 = []

list2.extend(a)
list2.extend(b)
list2.extend(c)

print(list2)

# how to print second list? elements are merged into one list.





#####ALTER THE LIST IN DIFFERENT WAYS#####
### Add a new list item = append

# letters.append("f")
# print(letters)

### Add a group of new items (needs to be added as a list)

# letters.extend(["g", "m"])
# print(letters)

### Inserts a new item in the index specified. Pushes everything forward. Values are not changed, a new item is added.
# letters.insert(1, "z")
# print(letters)

