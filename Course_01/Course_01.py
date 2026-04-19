# Exercise 01
# Ask for their name
# Say hi, (their name)

# name = input("Your Name: ")
# print(f"Hello, {name}")

# --------------------------------------------------------------------

# Exercise 02
# Ask for their name and their favorite color

# name = input("Your name please? ")
# print(f"Hi! {name}")
# color = input("What is your favorite color? ")
# print(f"So {name} likes {color} then...")

# --------------------------------------------------------------------

# Lessen 03
# Type conversion

# birth_year = input("What year were you are brought into this world? ")
# age = 2026 - int(birth_year)
# print(f"So your age is {age} then...")

# --------------------------------------------------------------------

# Exercise 03
# Ask for height in Cm
# Return it to foot and inch

# import math
# converion = 30.48
# height_cm = input("Your Height in Cm: ")
# height_ft = math.floor(int(height_cm) / converion)
# height_in = round(((int(height_cm) / converion) - height_ft) * 10)
# print(f"In America your height would be {height_ft}' {height_in}\" ")

# --------------------------------------------------------------------

# Lesson 04
# Long-form string

# message = """
# Hi there!

# I'm from Apex University, Nice to meet ya

# Best of luck,
# Random Guy

# """
# print(message)

# --------------------------------------------------------------------

# Lesson 05
# String index

# name = "Johanthan Browsey"
# print(name[0])
# print(name[5])
# print(name[-1])
# print(name[-3])
# print(name[0:6])

# --------------------------------------------------------------------

# Lesson 06
# String methods

# name = "Britney Helmfward"
# print(len(name))
# print(name.upper())
# print(name.lower())
# print(name.find("n"))
# print("Johny" in name)
# print("Britney" in name)

# --------------------------------------------------------------------

# Lesson 07
# Math operation

# import math

# x = 3.6
# y = 5.9

# print(math.ceil(x))
# print(math.floor(y))

# --------------------------------------------------------------------

# Lesson 08
# If statements

# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day,")
#     print("Please do your dehydration thingy.")
# elif is_cold:
#     print("It's a cold day,")
#     print("Please put on something for your warmthness.")
# else:
#     print("It's a wonderful day,")
# print("Enjoy your day while it's lasts...")

# --------------------------------------------------------------------

# Exercise 09

# Price of a house is $1M
# if the buyer has good credits
# they need to put down 10%
# otherwise
# they need to put down 20%
# print the down payment

# price_house = 1000000
# has_good_credits = False

# if has_good_credits:
#     down_payment = price_house * 0.1
# else:
#     down_payment = price_house * 0.2
# print(f"Your down payment: ${down_payment}")

# --------------------------------------------------------------------

# Lesson 10
# Logical operators

# has_high_income = True
# has_good_credits = False

# if has_high_income and has_good_credits:
#     print("Eligible for ma MONEY!")
# else:
#     print("GET OUTTA HERE!!")

# has_high_income = True
# is_student = True

# if has_high_income and not is_student:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# --------------------------------------------------------------------

# Lesson 11
# Comparison operators

# temperature = 30

# if temperature <= 30:
#     print("Today is not that hot.")
# else:
#     print("Today is DOOM!")

# --------------------------------------------------------------------

# Exercise 12
# If name is less than 3 characters long
# Name must be at least 3 characters
# Otherwise if name is more than 50 characters long
# Name can be at maximum 50 characters
# Otherwise
# Name is good

# name = input("Your name: ")

# if len(name) < 3:
#     print("Name must be at least 3 characters long!")
# elif len(name) > 50:
#     print("Name can be at maximum of 50 characters!!")
# else:
#     print(f"so your name is {name}? then, that's a good name yo.")

# while True:
#     name = input("Your name: ")
#     if len(name) < 3:
#         print("> Name must be at least 3 characters long!")
#     elif len(name) > 50:
#         print("> Name can be at maximum of 50 characters!!")
#     else:
#         break
# print(f"so your name is {name}? then, that's a good name yo.")

# --------------------------------------------------------------------

# Exercise 13
# Weight converter

# print("""
# ----------------------------
# Welcome to Weight Converter!
# ----------------------------
# """)

# weight = int(input("Your weight: "))
# unit = input("(L)Pound or (K)Kilogram?: ")
# converter = 2.205

# while unit.lower() == "l" or "k":
#     if unit.lower() == "l":
#         converted = weight / converter
#         print(f"You are {converted} kilograms")
#         break
#     elif unit.lower() == "k":
#         converted = weight * converter
#         print(f"You are {converted} pounds")
#         break
# else:
#     print("Please specify your input unit!")
# print("Done!!!")

# --------------------------------------------------------------------

# Lesson 14
# While loops

# i = 1
# while i <= 10:
#     print("#" * i)
#     i += 1
# print("Done!")

# --------------------------------------------------------------------

# Lesson 15
# Guessing Game

# guess_number = 6
# guess_count = 0
# guess_limit = 3

# while guess_count < 3:
#     guess = int(input("guess a number: "))
#     guess_count += 1
#     if guess == guess_number:
#         print("Congratulation! You Win!")
#         break
# else:
#     print("Sorry Bud! Next Time!")

# --------------------------------------------------------------------

# Lesson 16
# Car Game

# print("Welcome to Car Game!")
# print("Type help for more info.")

# command = ""
# is_started = False

# while True:
#     command = input("> ").lower()
#     if command == 'help':
#         print("""
# start -> start the car engine.
# stop -> to stop the car.
# quit -> to quit the program.
# """)
#     elif command == 'start':
#         if not is_started:
#             print("Starting the car engine...")
#             is_started = True
#         else:
#             print("The Car is already started!")
#     elif command == 'stop':
#         if is_started:
#             print("Stopping the car...")
#             is_started = False
#         else:
#             print("The Car is already stopped!")
#     elif command == 'quit':
#         print("Quitting the program...")
#         break
#     else:
#         print("Sorry! I don't understand...")

# --------------------------------------------------------------------

# Lesson 17
# For loops

# for item in 'VSCode':
#     print(item)

# for item in ['John', 'Jay', 'Joe']:
#     print(item)

# for item in [2, 3, 5, 7, 9]:
#     print(item)

# for item in range(2, 20, 4):
#     print(item)

# --------------------------------------------------------------------

# Exercise 18
# Use for loops to calculate the total price in a list

# prices = [67, 96, 129]
# total = 0
# print(f"item prices: {prices}")

# for item in prices:
#     total += item
# print(f"Total Price: {total}")

# --------------------------------------------------------------------

# Lesson 19
# Nested loops

# for x in range(3):
#     for y in range(5):
#         print(f"({x}, {y})")

# --------------------------------------------------------------------

# Exercise 20
# Make use of nested loops to print a letter F

# numbers = [5, 2, 5, 2, 2]

# for x_count in numbers:
#     print('x' * x_count)

# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'X'
#     print(output)

# Extra; try to print letter L

# numbers = [1, 1, 1, 1, 6]

# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'X'
#     print(output)

# --------------------------------------------------------------------

# Lesson 21
# Lists

# names = ['John', 'Jay', 'Joe', 'Fox', 'Aria']
# names[0] = 'Johny'

# print(names)

# --------------------------------------------------------------------

# Exercise 22
# Find the largest number in a list

# list = [1,2,3,21,6,7,8,9]
# max = list[0]
# for number in list:
#     if number > max:
#         max = number
# print(max)

# --------------------------------------------------------------------

# Lesson 23
# 2D lists

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # print(matrix[0][2])

# for row in matrix:
#     for item in row:
#         print(item)

# --------------------------------------------------------------------

# Lesson 24
# List methods

# numbers = [4, 6, 3, 8, 3, 9]

# numbers.append(12)
# print(numbers)

# numbers.insert(1,21)
# print(numbers)

# numbers.remove(9)
# print(numbers)

# numbers.pop()
# print(numbers)

# print(numbers.index(4))

# print(50 in numbers)
# print(8 in numbers)

# print(numbers.count(3))

# numbers.sort()
# print(numbers)

# numbers.reverse()
# print(numbers)

# numbers.clear()
# print(numbers)

# --------------------------------------------------------------------

# Exercise 25
# Remove duplicates in a list

# list = [1, 3, 3, 5, 6, 7, 8, 8, 9, 8, 37]
# no_dups = []

# for number in list:
#     if number not in no_dups:
#         no_dups.append(number)
#         print(no_dups)
#     else:
#         print(f'duplicate found! removing {number}')
#         print(no_dups)
# print(f'Result: {no_dups}')

# --------------------------------------------------------------------

# Lesson 26
# Tuples

# numbers = (2,4,6,8)
# numbers[0] = 10

# --------------------------------------------------------------------

# Lesson 27
# Unpacking

# coordinates = (1, 2, 3)

# # These 3 lines... 
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# # Are the same as this one
# x, y, z = coordinates

# print(x, y, z)

# --------------------------------------------------------------------

# Lesson 28
# Dictionary

# customer = {
#     "name": "John Sea",
#     "age": "67",
#     "is_old": True,
# }

# print(customer["name"])
# print(customer.get("age"))
# print(customer.get("birthdate","Dec 32"))

# --------------------------------------------------------------------

# Exercise 29
# Print a written number from a number input

# phone_number = input("Phone number: ")
# written_number = ""

# numbers_dictionary = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
# }

# for number in phone_number:
#     written_number += numbers_dictionary.get(number, "!ERROR!") + " " 
# print(written_number)

# --------------------------------------------------------------------

# Lesson 30
# Emoji Converter

# message = input("Your Message: ")
# words = message.split(' ')
# # # Check to see if spilt method works
# # print(words)
# emoji = {
#     ":)": "😀",
#     ":(": "😞",
# }
# output = ""

# for word in words:
#     output += emoji.get(word, word) + " "
# print(output)

# --------------------------------------------------------------------

# Lesson 31
# Custom Function

# def greeting():
#     print("Reception: Hello!")
#     print("Reception: Enjoy Your Stay!")

# print(">Entering the motel...")
# greeting()
# print(">Walking upstair...")

# --------------------------------------------------------------------

# Lesson 32
# Parameters

# def greeting(name, age):
#     print(f"Reception: Hello, {name}! and you are {age} years old!")
#     print("Reception: Enjoy Your Stay!")

# print(">Entering the motel...")
# greeting("John", "25")
# greeting("Aria", "27")
# print(">Walking upstair...")

# --------------------------------------------------------------------

# Lesson 33
# Keyword Arguments
# The order of the argument is ignored becuase it is already defined in the argument input.

# def greeting(name, age):
#     print(f"Reception: Hello, {name}! and you are {age} years old!")
#     print("Reception: Enjoy Your Stay!")

# greeting(age="25", name="John")

# Key take away: Try to use Positional arguments most of the time.
# Keyword arguments only get used when trying to make code more readable or when your input can switch positions.
# Keyword arguments should come after Positional arguments if you need to use both of them.

# --------------------------------------------------------------------

# Lesson 34
# Return Statement

# def sqaure(number):
#     return number * number

# print(sqaure(5))

# --------------------------------------------------------------------

# Exercise 35
# Creating a resuable function

# Emoji Converter: Test :( :)

# def emoji_converter(message):
#     words = message.split(' ')
    
#     emoji = {
#         ":)": "😀",
#         ":(": "😞",
#     }

#     output = ""
    
#     for word in words:
#         output += emoji.get(word, word) + " "
#     return output


# message = input("Your Message: ")
# print(emoji_converter(message))

# --------------------------------------------------------------------

# Lesson 36
# Exceptions

# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid Value! Please Try Again!')

# --------------------------------------------------------------------

# Lesson 37
# Comments

# # What does this do?
# # This is a comments.
# print("Hello?")

# --------------------------------------------------------------------

# Lesson 38
# Classes

# # Usually we use title_title to name variables
# # TitleTitle -> this is called Pascal naming convention
# class PointCloud:
#     def move(self):
#         print("Moving Pointclouds...")
#     def delete(self):
#         print("Deleting Pointclouds...")


# custom_class = PointCloud()
# custom_class.move()
# custom_class.delete()

# # You can add more attributes to a variable that uses those classes.
# point01 = PointCloud()
# point01.x = 10
# point01.y = 20
# print(point01.x)
# print(point01.y)

# --------------------------------------------------------------------

# Lesson 39
# Constructors

# Init line is what's called Constructor 

# class PointCloud:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("Moving Pointclouds...")
#     def delete(self):
#         print("Deleting Pointclouds...")


# point = PointCloud(12,24)
# print(point.x)
# print(point.y)
# point.x = 67
# point.y = 87
# print(point.x)
# print(point.y)

# --------------------------------------------------------------------

# Exercise 40
# Create a new class called Person
# It should have a name attribute
# And a talk() Method

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f'Hello, {self.name} talking.')

# people01 = Person('John Connor')
# people01.talk()

# people02 = Person('Jimm Putdown')
# people02.talk()

# --------------------------------------------------------------------

# Lesson 41
# Inheritance

# class Mammal:
#     def walk(self):
#         print('Walking...')

# # Use class(ParentClass) format for inheriting a parent class methods
# # Use pass to let python skips empty classes
# class Dog(Mammal):
#     pass

# # If the class is not empty, just define a method as usual.
# class Cat(Mammal):
#     def purring(self):
#         print('Purring...')


# dog01 = Dog()
# dog01.walk()

# cat01 = Cat()
# cat01.walk()
# cat01.purring()

# --------------------------------------------------------------------

# Lesson 42
# Modules

# def cm_to_m(length):
#     return length * 100

# def m_to_cm(length):
#     return length / 100

# Function above is moved to Course_01_Lesson_42_Modules.py

# # One way of importing another python script
# import Course_01_Lesson_42_Modules
# print(Course_01_Lesson_42_Modules.m_to_cm(23))

# # Another way
# from Course_01_Lesson_42_Modules import cm_to_m
# print(cm_to_m(5600))

# --------------------------------------------------------------------

# Exercise 43
# Create a find_max function and put it in a separate module called utils.py
# Called the function into the main app and print the result

# from Course_01_Exercise_43_Modules import find_maximum

# list = [1,5,7,23,64,89,105]
# print(find_maximum(list))

# --------------------------------------------------------------------

# Lesson 44
# Packages

# Think of it like a section in a store
# |- Section
#    |- Sports
#       |- Football, Gloves etc.

# |- Package
#    |- Modules
#       |- Functions, Classes etc.

# # This method of importing a module in a package is okay but it's a little long.
# # If you have to call it multiple times, you'll have to call out its full path.
# import pack_ecommerce.shipping

# pack_ecommerce.shipping.calc_shipping()

# # This one it better and and shorter
# from pack_ecommerce.shipping import calc_shipping, module01, module02

# calc_shipping()
# calc_shipping()
# calc_shipping()

# # Or you can use this method to import the whole module.
# # And access its function manually.
# from pack_ecommerce import shipping

# shipping.calc_shipping()

# --------------------------------------------------------------------

# Lesson 45
# Python module index
# Generating random values

# You can look it up online using 'Python 3 module index' search.

# import random

# # Random function generates a random real number from 0 to 1.
# for x in range(5):
#     print(random.random())

# # Use randint for integer, and it can be used in range too.
# for y in range(4):
#     print(random.randint(10,50))

# # Use choice to select a random item from a list.
# candidates = ['John', 'Durham', 'Jay', 'Aria', 'Artem', 'Amilia']
# leader = random.choice(candidates)
# print(leader)

# --------------------------------------------------------------------

# Exercise 46
# Roll the dice
# Create a new Dice class with a roll function that is a tuple of two numbers

# import random


# class Dice:
#     def roll(self):
#         x = random.randint(1, 6)
#         y = random.randint(1, 6)
#         return x,y
        

# dice01 = Dice()
# print(dice01.roll())

# --------------------------------------------------------------------

# Lesson 47
# Working with directories

# Absolute Path
# c:\Program Files\Microsoft
# /usr/local/bin

# Relative Path
# ../../ecommerce

# from pathlib import Path

# path01 = Path('pack_ecommerce')
# print(path01.exists())

# # Use glob to search for files or file with specific extension
# path = Path()
# for file in path.glob('*'):
#     print(file)

# print('----------------------')

# for file in path.glob('*.py'):
#     print(file)

# --------------------------------------------------------------------

# Lesson 48
# PyPI
# Install external python packages

# In terminal type -> pip install openpyxl

# --------------------------------------------------------------------

# Project 49
# Excel automation with python

# import as is a way to give it a new nickname, so it's easier for you to call it later.
# import openpyxl as xl

# Import a BarChart and a Reference classes to create a bar chart later on.
# from openpyxl.chart import BarChart, Reference

# Use a load workbook function to load an excel file.
# wb = xl.load_workbook('Course_01/transactions.xlsx')

# This is how to access a certain sheet in excel, and it is case sensitive.
# sheet = wb['Sheet1']

# This is how to acces a certain cell in a sheet.
# cell = sheet['a1']
# print(cell.value)

# Or you can call a cell method an input a cell coordinates.
# cell1 = sheet.cell(1,2)
# print(cell1.value)

# A method to show how many row/column there are in a sheet.
# print(sheet.max_column)
# print(sheet.max_row)

# We need to iterate through every row in a certain column to automate this.
# We use 2 and max row + 1 because...
# we don't need the header and range function only count up to n-1.
# for row in range(2, sheet.max_row + 1):
    # print(row)
    # cell = sheet.cell(row, 3)
    # print(cell.value)
    # corrected_price = cell.value * 0.9
    # corrected_price_cell = sheet.cell(row, 4)
    # corrected_price_cell.value = corrected_price

# chart_value = Reference(sheet,
#                         min_row=2,
#                         max_row=sheet.max_row,
#                         min_col=4,
#                         max_col=4)
# chart = BarChart()
# chart.add_data(chart_value)
# sheet.add_chart(chart, 'e2')

# wb.save('Course_01/transactions2.xlsx')

# --------------------------------------------------------------------

# Our code above is a bit messy.
# Let's try to clean that up.
# And it's only working on a specific file that we input in a load workbook function.
# Let's change that to a function to automate that too.

# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference

# def process_workbook(filename):
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet1']

#     for row in range(2, sheet.max_row + 1):
#         cell = sheet.cell(row, 3)
#         corrected_price = cell.value * 0.9
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price

#     chart_value = Reference(sheet,
#                             min_row=2,
#                             max_row=sheet.max_row,
#                             min_col=4,
#                             max_col=4)
#     chart = BarChart()
#     chart.add_data(chart_value)
#     sheet.add_chart(chart, 'e2')

#     wb.save(filename)