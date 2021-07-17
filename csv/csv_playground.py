# import csv

#

# with open ("dogs_are_awesome.txt") as csv_file:
#     csv_reader = csv.reader(csv_file) #creates the reader object
#     for line in csv_reader:
#         print(line)


# import csv

# asli_said = []

# with open ("dogs_are_awesome.txt") as csv_file:
#     csv_reader = csv.reader(csv_file) #creates the reader object
#     for line in csv_reader:
#         # print(line)
#         asli_said.append(line) 

# print(asli_said)

# with open("asli_says.txt", mode = "w", newline="") as csv_file: 
# #if file doesnt exist it will be created, if it exists, it will be overwritten
#     csv_writer = csv.writer(csv_file) #creates the writer object
#     for item in asli_said:
#         csv_writer.writerow(item)

# read the file, saved the file in a list, wrote the new file.

