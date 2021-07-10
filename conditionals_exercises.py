####Q1#####

moths_in_house = False

if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")

####Q2#####

moths_in_house = False
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")
elif moths_in_house and not mitch_is_home:
    print("Meoooooowwww! Hissssss!")
else:
    print("Climb on Mitch.")

####Q3#####

light_colour = "Amber"
car_detected = False

if light_colour == "Red" and car_detected:
    print("Flash!")
else:
    print("Do nothing.")

####Q4#####

height = input("How tall are you? ")

if int(height) >= 120:
    print("Hop on!")
else:
    print("Sorry, not today :(")

####Q5#####

username = "fleur"
password = "password123"

enter_user = input("Username: ")
enter_pass = input("Password: ")

if enter_user == username and enter_pass == password:
    print("Correct!")
else:
    print("Incorrect!")

#####Q6#####

enter_email = input("Email: ")

if "@" in enter_email and "." in enter_email:
    print("Valid email address.")
else:
    print("Invalid email address.")
