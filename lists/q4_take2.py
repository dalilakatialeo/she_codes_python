#first list

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

list1 = [a,b,c]
print(list1)

# can also be done like this!
list1 = []
list1.extend([a,b,c])
print(list1)


#second list
list2 = []

list2.extend(a)
list2.extend(b)
list2.extend(c)
print(list2)