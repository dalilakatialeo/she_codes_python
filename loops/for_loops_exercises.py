# Q1

# num = input("Enter a number: ")

# for number in range(int(num) + 1):

#     multiply = int(number) * (int(num)+1)
#     print(f"{num} * {number} = {multiply}")


# answer = input("Enter a number: ")
# # for answer in range(int(number)):
# #     print(f"str{answer} * {+1}

# num = input("Enter a number: ")
# for n in range(int(num) + 1 ):
#     print(f"{num} * {n} = ", int(num) * int(n))

# Bruna's solution:

# num= input("Enter a number: ")
# for n in range(int(num)):

#     print(f"{num} * {n + 1} = ", int(num) * int(n + 1))

    # what is the reasoning behind this?
    # also, seems incorrect - how to get rid of firstline "* 0"?



#Q2

num = input("Enter a number: ")

total = 0

for n in range(int(num) + 1):
    total = total + n
print(total)

# what am i doing wrong? I only want to print the last one!

# Q3

random_numbers = []

total = 0


for number in random_numbers:
    total = total + number  
print(total)


# lost.....


# #Q4

# mailing_list = [
#     ["Chilli", "chilli@thechihuahua.com"],
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Ivy", "noreply@goldendreamers.xyz"],
# ]


# for item in mailing_list:
#     print(f"{item[0]}: {item[1]}")