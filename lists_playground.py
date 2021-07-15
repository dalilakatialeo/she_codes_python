letters = ["a", "b", "c", "d", "e"]
# # print(letters[3])
# # print(letters[-1]) #-1 always returns the last value of the list
# # print(letters[-2]) #-2 always returns the second last value of the list

# # print(letters[0:3])
# # print(letters[3])
# # print(letters[1:3]) #slicing always excludes the last one
# # print(letters[1:5:3])

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

#######indexing
# print(len(chilli_wishlist)) #parsing to see how many elements are in the list
# print(chilli_wishlist)
# print(type(chilli_wishlist))

# print(chilli_wishlist[0])
# print(chilli_wishlist[1])
# print(chilli_wishlist[-1])

#######slicing
# print(chilli_wishlist[0:2])
# print(chilli_wishlist[1:3])

# chilli_wishlist[-1] = "strawberry"
# print(chilli_wishlist)


########CHALLENGE########
#print sublist (a list extracted from the main list, done by slicing)
#print sublist of items in position 2 through 3
#print the item in index -3
#change the value of the first item in the list

# print(chilli_wishlist[2:4])
# print(chilli_wishlist[-3])

# chilli_wishlist[1] = "tennis ball"
# print(chilli_wishlist)

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

### Value in that position is removed.
# letters.pop(2)
# print(letters)

### Specified value is removed.
# letters.remove("d")
# print(letters)

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# chilli_wishlist.append("dig mat")
# chilli_wishlist.extend(["kong", "tennis ball", "crocodile toy"])
# chilli_wishlist.remove("igloo")
# print(chilli_wishlist)


# if "tennis ball" in chilli_wishlist:
#     print("Chilli would like a tennis ball")
# else:
#     print("Chilli doesn't feel like playing fetch.")


# if len(chilli_wishlist) > 8:
#     print("Chilli wants a lot of stuff!")

chilli_wishlist = [
    ["igloo"],
    ["donut toy", "tennis ball", "crocodile toy"],
    ["chicken", "peanut butter"],
    ["cardboard box", "box", "dig mat"]
]

print(len(chilli_wishlist))
print(chilli_wishlist [2][0])
print(chilli_wishlist[-1][-1])