# A function is a block of reusable code that performs a specific task.

def greet():
    print("Hello, World!")

greet()

def addition(a, b):
    return a + b

result = addition(45, 32)

print(result)

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("Ali")    # Output: Hello, Ali!

def square(a):
    return a * a

for i in range(10):
    print(f"The square of {i} is {square(i)}")

def count_to(n):
    for i in range(1, n + 1):
        print(i)

count_to(5)  

def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(7) 

# A module is a file that contains Python code: functions, classes, or variables. You can import and use it in other Python files.
import math

print(math.sqrt(16))       # Output: 4.0
print(math.pi)             # Output: 3.14159...

