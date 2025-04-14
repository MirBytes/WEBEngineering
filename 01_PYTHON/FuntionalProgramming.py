# Functional Programming (FP) is a coding style where you treat functions as first-class citizens and avoid changing state or mutating data. In short:
#     Use pure functions (no side effects)
#     Prefer immutability (don’t modify variables)
#     Use higher-order functions (functions that take or return other functions)
#     Rely on map, filter, reduce, and lambda for clean, functional-style code

# Frist Class Programming: Functions can be assigned to variables, passed as arguments, and returned from other functions.

def greet(name):
    return f"Hello, {name}"

say_hello = greet
print(say_hello("Teymur"))

# Lambda Function

square = lambda x : x * x 
print(square(5))

# MAP: Used to apply a function to every item in a list (or iterable).

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)

# Filters: Filters items in a list based on a condition.

nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4, 6]

# Reduce: Applies a function cumulatively to the items — like combining everything into a single value.

from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)

#Decorators: One thing made possible by functional programming is the idea of a decorator, which is a higher-order function that can modify another function. 

def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, BAJWA SB")

hello()

people = [
    {"name": "Harry", "House": "Motra"},
    {"name": "Teymur", "House": "Gujrawala"},
    {"name": "Rana", "House": "Kang"}
]

people.sort(key = lambda person: person["name"])

print(people)

# Exceptions

x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} = {result}")

import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")


import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")
