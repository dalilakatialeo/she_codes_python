#solution 1 : individually append items

name1 = input ("Enter a name: ")
name2 = input ("Enter a name: ")
name3 = input ("Enter a name: ")

list = []

list.append(name1)
list.append(name2)
list.append(name3)
print(list)

#solution 2: extend items as a group

list.extend([name1,name2,name3]) #more efficient and DRIER! (FEWER LINES)
print(list)
