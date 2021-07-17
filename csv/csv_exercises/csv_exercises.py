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

#######Q2

# with open("colours_20_simple.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     headers= next(csv_reader)
#     for line in csv_reader:
#         print(f"{line [2]}, Hex: {line[1]}, RGB: {line[0]}")
        # colour_list2.append(line)
        # print(line)

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

with open("galaxies.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        velocity = []
        for galaxy in csv_reader:
                velocity.append(galaxy [1])
