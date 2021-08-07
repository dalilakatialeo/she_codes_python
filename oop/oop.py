name = "Asli"
age = 26
print(type(name)) # class str
print(type(age)) # class int


# variable followed by . opens a library of functions
print(name.upper()) # uppercase
print(dir(name)) # lists the built in functions available to that variable (in this case, a string)

# abstract data type - you can build your own class

# OOP - Object Oriented Programming (everything that exists in Python is an object)
# Once we build a class, we can create an object from a class

class Dog: #created a class called "Dog", starts with upper case, written out in CamelCase.
    # We are building the blue print of the object
    #technically a function, but if it belongs to a class its called a METHOD. Can only be used on an instance (= object) of the class. It defines actions or functionalities (e.g. TALK, WALK, PLAY)
    def __init__(self, age, breed): #this is to initialise the object
        #whenever we define a method, the first parameter is SELF - its never passed as a value
        # age and breed are ATTRIBUTES
        self.age = age
        self.breed = breed

    def talk(self):
        return "Bark"

#creating an object from that class - all the methods defined within the class can be applied to those objects
Jett = Dog(3, "pug") # creation of the instance. 
Jett.talk()
Chilli = Dog(4, "chi")
Chilli.talk()
