import csv

######Q1
# colour_list = []

# with open("colours_20_simple.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         colour_list.append(line)

# # print(colour_list)

# for row in colour_list:
#     print(f"{row [0]} {row[1]} {row[2]}")

# colour_list2 = []

# #######Q2

# with open("colours_20_simple.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     headers= next(csv_reader)
#     for line in csv_reader:
#         print(f"{line [2]}, Hex: {line[1]}, RGB: {line[0]}")
#         colour_list2.append(line)
#         print(line)

# print(colour_list2)

# for row in colour_list2:
    

#########Q3

# with open("colours_20.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     headers= next(csv_reader)
#     for line in csv_reader:
#         print(f"{line [4]}, Hex: {line[2]}, RGB: {line[1]}")


##########Q4
# with open("colours_213.csv") as csv_file:
#         csv_reader = csv.reader(csv_file)
#         red = 0 #initiating counter
#         green = 0
#         blue = 0
#         yellow = 0
#         for i, line in enumerate(csv_reader):
#                 if i !=0:
#                         if "red" in line[4]:
#                                 red += 1
#                         if "green" in line[4]:
#                                 green += 1
#                         if "blue" in line[4]:
#                                 blue += 1
#                         if "yellow" in line[4]:
#                                 yellow += 1
#         print(f"Red: {red} \nGreen: {green} \nBlue: {blue} \nYellow: {yellow}")

##########Q5

# list = []

# # max_velocity == max(galaxies[1])

# with open("galaxies.csv") as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for galaxy in csv_reader:
#               list.append(galaxy) # created a list, populated with galaxy data sublists

# for l in list:
#         for i in l[1]:
#                 new_list = [max(i) for i in l[1]]
# print(new_list)
# # for line in list:

        
# with open('galaxies.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     slow = [None, float('inf')]
#     fast = [None, 0]
#     for i, row in enumerate(csv_reader):
#         if i != 0:
#             if int(row[1]) < slow[1]:
#                 slow =  [row[0], int(row[1])]
#             if int(row[1])> fast[1]:
#                 fast = [row[0], int(row[1])]
#     print(f'Galaxy {slow[0]} has a min velocity of {slow[1]}km/sec.')
#     print(f'Galaxy {fast[0]} has a max velocity of {fast[1]}km/sec.')

# sorted(list[1])
#         for line in enumerate(galaxies):
#                 if line != 0:
#                         for i in line:
#                                 if i[1] == min(line[1]):
#                                         print(f"Galaxy {i[0]} has the min velocity of {i[1]} km/sec.")
# #                 if data == max(galaxies[1]):
#                         print(f" Galaxy {galaxies[0]} has the max velocity of {galaxies[1]} km/sec.")

# print(max (galaxies[1][1]))

        # for i, line in enumerate(csv_reader):
        #         if i !=0:
        #                 if i == min(line[1]):
        #                         print(i)
        #                 if i == max(line[1]):
        #                         print(i)
        # print(max_velocity)
                        # print(f"Galaxy {data[0]} has the min velocity of {data[1]}km/sec.")
#                 if d in data[1]== max(data[1]):
#                         print(f"Galaxy {data[0]} has the max velocity of {data[1]}km/sec.")
# # print(galaxies)



######Q5 retry

with open('galaxies.csv')


with open('galaxies.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    slow = [None, float('inf')]
    fast = [None, 0]
    for i, row in enumerate(csv_reader):
        if i != 0:
            if int(row[1]) < slow[1]:
                slow =  [row[0], int(row[1])]
            if int(row[1])> fast[1]:
                fast = [row[0], int(row[1])]
    print(f'Galaxy {slow[0]} has a min velocity of {slow[1]}km/sec.')
    print(f'Galaxy {fast[0]} has a max velocity of {fast[1]}km/sec.')
