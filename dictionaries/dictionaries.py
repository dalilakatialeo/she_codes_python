students = ["Angela", "Jen", "Bel"]
# print(students[0]) # extracted a value with indexing

#creating a dictionary, separated with comma
#elements are key:value pairs
#keys need to be unique, keys can be only immutable data types (once created, it cant be changed e.g. String, Integer, Float, Bool, List)
#Values dont need to be unique, any data type
#dictionaries are unordered

students_dict = {"Angela": 1, "Jen": 2, "Bel": 3}
print(students_dict.get("Bel")) #can take 1 or 2 parameters
# print(students_dict["Asli"]) #same as doing this, however Key Asli doesnt exist, so it will output error
print(students_dict.get("Asli", 15)) #try get Bel, if doesnt exist, print 0 - avoids outputting error
print(students_dict.get("Asli", "Hi!"))
# print(students_dict["Asli"]) #Key Asli doesnt exist, so it will output error

# print(students_dict)

#extract a value
#print(students_dict["Angela"])

#add a key:value
students_dict["Asli"] = 4
# print(students_dict)

#if key already exists - it replaces it
students_dict["Jen"] = 10
# print(students_dict)

#delete a key:value pair
del students_dict["Asli"]
# print(students_dict)

#when do we use this data storage type?
#counting something, unique kyes etc

# print(students_dict.keys()) # prints all the keys (inbuilt function)
# print(students_dict.items()) # prints couples of keys and values - useful when we loop through a dict


#iteration
# for key in students_dict:
#     print(key, students_dict[key])

    #we looped thru a dict and each time we have printed key and value

# for key, value in students_dict.items():
#     print(key,value)

#checks the item (made by the couple key:value)
#the two for loops abolve do the same thing.