import random
import asyncio
import httpx 

              # Lesson 1: Introduction to Python
                    #     - What is Python?
                    #     - Installing Python?
                    #     - Running Python code.

                    #     - Exercise Prin('hello, world')

# print('hello world')


                    # Lesson 2: Variables and Data Types
                    #     - Variables
                    #     - Basic Data Types (int, float, str, bool)
                    #     - Type conversion
                    #     - Create Variables for your name, age, and favorite number, then print them


                    # int is a integer that represents whole numbers
                    # float represents decimal numbers such as 0.03
                    # str represents text
                    # bool represents boolean values such as true or False

# age = 32
# name = 'Alison'
# favorite_number = 37

# print(str(age), name, favorite_number)


                    # # Lesson 3 and 11: Basic Operations and input
                    #     - Arithimetic operators
                    #     - Comparison operators
                    #     - Getting uer input using input

                    #     - Excercise create a simple calculator that takes numbers as input and performs basic arithmetic operations



# def calculator_operation(num1, num2, operator):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '/':
#         if num1 == 0 or num2 == 0:
#             return None
#         return num1 / num2
#     elif operator == '*':
#         if num1 == 0 or num2 == 0:
#             return None
#         return num1 * num2
#     else:
#         return None


# def float_inputs():
#     while True:
#         print("Enter a number:")
#         try:
#             num = float(input())
#             return num
#         except ValueError:
#             print("Invalid input, must be a number")

# def operator_input():
#     print("Enter an operator")
#     operator = input()
#     while True:
#         try:
#             assert operator in ['+', '-', '*', '/']
#             return operator
#         except AssertionError:
#             print("Invalid Operator")

# num1 = float_inputs()
# num2 = float_inputs()
# operator = operator_input()


# result = calculator_operation(num1, num2, operator)

# if result is not None:
#     print(f"The result is {result}")
# else:
#     print("Invalid input")


                    # Lesson 4: Strings and String Manipulation
                    #     - String indexing and slicing
                    #     - String concatenation
                    #     - String methods

                    #     - Excercise: Take a string as input and reverse it

# #Slice the message in reverse order
# def string_reverse(text):
#     return text[::-1]

# print("Enter a message")
# message = input("")
# message_reversed = string_reverse(message)

# print("Message reversed", message_reversed)

# #skips every other letter
# def string_skip(text):
#     return text[::2]

# message_skipped = string_skip(message)

# print("Message skipped", message_skipped)



                    # Lesson 5 Control Structures
                        # - if, elif and else statements
                        # - while loops
                        # - for loops
                        # - Excercise write a program that prints the numbers from 1 to 100 but for multiples of 3
                        # - for multiples of 5 print Buzz

                        # - for numbers which are multiples of both 3 and 5 print FizzBuzz


# def control_structure():
#     for i in range(0, 100):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)


# control_structure()


                    # Lesson 6: Lists
                    #     - Creating Lists
                    #     - List indexing and slicing
                    #     - List methods
                    #     - List Comprehensions

                    #     - Excercise: Given a list of numbers create a new list containing the squares of the original numbers

# list_numbers = [1, 6, 9, 4, 8, 24]

# def list_numbers_square(numbers):
#     squares = []

#     for num in numbers:
#         square = num ** 2
#         squares.append(square)
#     print(squares)
#     return squares

# list_numbers_square(list_numbers)


                    # Lesson 7: Tuples and Sets
                    #     - Creating Tuples
                    #     - Tuple Unpacking
                    #     - Creating Sets
                    #     - Set operations

                    #     - Excercise remove duplicates from a given list using sets

# main_list = [1,2,5,3,3,5,6,5,6,5,8,21,23,1,21,21,22]

# list_as_set = set(main_list)

# list_unique = list(list_as_set)

# print(list_unique)


                    # Lesson 8: Dictionaries 
                    #     - Creating Dictionaries
                    #     - Accessing and modifying dictionary values
                    #     - Dictionary Methods

                    #     - Excercise: Create a simple dictionary to store student names and their gades, then print the dictionary

# student_grades = {"alison": 100, "Jordan": 46, "Charles": 76, "Brit": 90}

# print(student_grades)

# for key in student_grades:
#     print(f"{key}: {student_grades[key]}")


                    # Lesson 9: Functions
                    #     - Defining 
                    #     - Functions arguments and default values
                    #     - Return Values

                    #     Excercise: Write a function to calculate the factorial of a given number


# def factorial(n):
#     if n == 0:
#         return 1  
#     else:
#         return n * factorial(n - 1)

# result = factorial(8)

# print(result)


                    # Lesson 10: Modules and Libraries
                    #     - Importing modules
                    #     - Standard libraries
                    #     - Installing and using third-party libraries

                    #     - Excercise: write a program that generates and prints a random number between 1 and 100 using the 'random' Module

# def random_number():
#     x = random.randint(1, 100)
#     print(x)

# random_number()


                    # Lesson 11: Error Handling
                    #     - Syntax errors vs exceptions
                    #     - Try except and finally statements
                    #     - Raising exceptions

                    #     Excercise: Modify the simple calculator to handle division by zero exceptions

# Refer to lesson 3


                    # Lesson 12: File I/O
                    # - Opening and closing files
                    # - Reading and writing to files 
                    # - Working with csv files

                    # - Excercise: Read a text file and count the number of lines words and characters in the file



# filename = 'sample_text.txt'
# with open(filename, 'r') as file:
#     contents = file.read()

#     num_lines = len(contents.split('\n'))
#     num_words = len(contents.split())
#     num_chars = len(contents)

# print("number of lines", num_lines)
# print("Number of words:", num_words)
# print("Number of characters:", num_chars)



                    # Lesson 13: Classes and Objects
                    #     - Defining classes and creating objects
                    #     - Instance variables and methods
                    #     - inheritance and polymorphism

                    #     - Excercise: Create a class hierarchy for different types of vehicles(e.g. car,truck,motorcycle) with common attributes and methods

# class vehicle:
#     def __init__(self, make, model, year):
#         self._make = make
#         self._model = model
#         self._year = year


#     def vechicle_year_correction(self, year):
#         self._year = year


# class car(vehicle):
#     def __init__(self, make, model, year, color):
#         super().__init__(make, model, year)
#         self._color = color


# class truck(vehicle):
#     def __init__(self, make, model, year, color):
#         super().__init__(make, model, year)
#         self._color = color


# vehicle1 = vehicle("Pontiac", "G6", 2008)
# print(vehicle1._year)
# vehicle1.vechicle_year_correction(2009)
# print(vehicle1._year)


                    # Lesson 14: lambdas and Higher Order Functions
                    #     - Lambad functions
                    #     - map(), filter(), and reduce() functions
                    #     - Using Lambdas with higher order functions

                    #     - Excercise: Use a lambad function with the filter() function to find the even numbers in a given list

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# print(even_numbers)


                    # Lesson 15: List Comphrensions Revisited
                    #     - Conditional list comprehensions
                    #     - Nested list comprehensions

                    #     - Exercise: Create a list comprehension that generates a list of tuples containing pythagorean triples (a,b,c) where a, b


# Lesson 16:  Asynchronous Programming
#     - Introduction to Asynchronous Programming
#     - Async/await
#     - Coroutines

#     - Exercise: Write a program that uses asyncio to asynchronously download several web pages and prints 
#                 out their content


async def fetch_page(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text
    
async def main():
    urls = [
        'https://www.teamliquid.com',
    ]

    tasks = [fetch_page(url) for url in urls]
    pages = await asyncio.gather(*tasks)

    for page in pages:
        print(page)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



