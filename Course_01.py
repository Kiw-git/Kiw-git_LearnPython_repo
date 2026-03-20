# exercise 01
# ask for their name
# name say hi, (their name)

# name = input("Your Name: ")
# print(f"Hello, {name}")

#--------------------------------------------------------------------

# exercise 02
# ask for their name and their favorite color

#name = input("Your name please? ")
#print(f"Hi! {name}")
#color = input("What is your favorite color? ")
#print(f"So {name} likes {color} then...")

#--------------------------------------------------------------------

# lessen 03
# Type conversion

#birth_year = input("What year were you are brought into this world? ")
#age = 2026 - int(birth_year)
#print(f"So your age is {age} then...")

# exercise 03
# ask for height in Cm
# return it to foot and inch

import math
converion = 30.48
height_cm = input("Your Height in Cm: ")
height_ft = math.floor(int(height_cm) / converion)
height_in = round(((int(height_cm) / converion) - height_ft) * 10)
print(f"In America your height would be {height_ft}' {height_in}\" ")
