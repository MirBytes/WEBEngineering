print("Hello World")

# Some of the most common variable types are:

#     int: An integer
#     float: A decimal number
#     str: A string, or sequence of characters
#     bool: A value that is either True or False
#     NoneType: A special value (None) indicating the absence of a value.

a = 23
name = "AHMED ALI"
x = 3.14
d = None
e = True

name = input ("Name : " )
print("Hey " + name)

# print(f"SO, you are, {name}")
# print(f"Again Hello, {input ('Hello: ')} , Enter a Number Below!")

# Now, Let's go through the conditional statements.

num = int(input("Number: "))
if num > 5:
    print(f"The {num} is greater then 5")
elif num < 5:
    print(f"The {num} is less then 5")
else:
    print(f"The {num} is equal to 5")

# A sequence is an ordered collection of items that can be accessed by index.
# Mutable means that once a sequence has been defined, we can change individual elements of that sequence, and ordered means that the order of the objects matters.

# The most common sequence types are lists and tuples.
# Lists are mutable, while tuples are immutable.
# Lists are defined by square brackets [], and tuples are defined by round brackets ().
# Lists are ordered, and items in a list can be of any data type, including strings,
# Tuples are also ordered, but items in a tuple must be of the same data type.

names = ["Ibrhaim", "Ahmed", "Taimoor"]
print(names[0])

print(names)

names.append("MIR")

print(names)
# The most common methods for lists are:
# append() : Adds an element to the end of the list.
# insert() : Inserts an element at a specified position in the list.
# remove() : Removes the first occurrence of the value.
# pop() : Removes and returns the element at the specified position in the list.
# index() : Returns the index of the first occurrence of the value.
# count() : Returns the number of occurrences of the value.
# sort() : Sorts the list in ascending order.
# reverse() : Reverses the list.
# clear() : Removes all elements from the list.
# extend() : Adds all elements from the specified list to the end of the current list.
# copy() : Returns a copy of the list.
# join() : Concatenates all items in the list into a single string.

names.insert(2, "Jilani")
print(names)

names.sort()
print(names)

numbers = [34, 45, 65, 222]

names.extend(numbers)
print(names)


# The most common methods for tuples are:
# count() : Returns the number of occurrences of the value.
# index() : Returns the index of the first occurrence of the value.

point = (12.45, 98.11)
print(point.count(12.45))

# The other more common methods for strings are:
# capitalize() : Converts the first character of the string to uppercase and makes all other characters in the string lowercase.
# casefold() : Converts the string to lowercase.
# center() : Returns a centered string.
# count() : Returns the number of occurrences of the value.
# encode() : Returns a bytes object containing the encoded version of the string.
# endswith() : Returns True if the string ends with the specified value, otherwise False.
# expandtabs() : Replaces all tab characters in the string with spaces.
# find() : Returns the index of the first occurrence of the value.
# format() : Formats the string according to the specified format.
# index() : Returns the index of the first occurrence of the value.
# isalnum() : Returns True if all characters in the string are alphanumeric, otherwise False.
# isalpha() : Returns True if all characters in the string are alphabets, otherwise False
# isdecimal() : Returns True if all characters in the string are decimals, otherwise False.
# isdigit() : Returns True if all characters in the string are digits, otherwise False.
# islower() : Returns True if all characters in the string are lowercase, otherwise False.
# isnumeric() : Returns True if all characters in the string are numeric, otherwise False.
# isprintable() : Returns True if all characters in the string are printable, otherwise False.
# isspace() : Returns True if all characters in the string are whitespace, otherwise False.
# istitle() : Returns True if the string follows the rules of a title case string, otherwise
# isupper() : Returns True if all characters in the string are uppercase, otherwise False.
# join() : Concatenates all items in the list into a single string.

seq = [1, 2, 3, 4, 5]

# Indexing
print(seq[0])  # First element

# Slicing
print(seq[1:4])  # [2, 3, 4]

# Length
print(len(seq))  # 5

# Membership test
print(3 in seq)  # True

# Concatenation
print([1, 2] + [3, 4])  # [1, 2, 3, 4]


# A set is an unordered, unindexed collection of unique elements.
# dublicates are removed and in sequence
s = set()
s = {23, 56, 22, 56}
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
s.add(5)
s.add(4)

s.remove(6)

print(s)

print(f"The lenght of set s is {len(s)}")

# Create a set of students
students = {"Ali", "MIR", "Ahmed", "MIR"}  # 'MIR' will appear only once

# Add a new student
students.add("BAJWA")

# Check membership
print("Ali" in students)  # True

# Combine two sets of classes
class_A = {"Ali", "JILNAI"}
class_B = {"JILNAI", "Bilal"}
print(class_A | class_B)  # Union: {'Ali', 'JILNAI', 'Bilal'}

# A dictionary is a collection of key-value pairs.
#     Keys are unique.
#     Values can be any type.
#     Syntax: {key: value}

ANIME = {
    "NARUTO" : "Naruto",
    "ONE PIECE" : "LUFFY",
    "DRAGON BALL" : "SON GOKU/ KAKAROTT"
}

print(ANIME["NARUTO"])  # Output: Naruto
# Add a new anime
ANIME["BLEACH"] = "ICHIGO"
print(ANIME)

SASUKE = {
    "Sasuke" : "Uchiha",
    "Age" : 22,
    "Occupation" : "Ninja",
    "Personality" : "Sarcastic",
    "Friends" : ["Sakura", "Naruto"],
    "Sensei" : "Kakashi"
}

print(SASUKE["Sasuke"])

del ANIME["DRAGON BALL"]
ANIME.pop("BLEACH")

SASUKE.keys()     # All keys
SASUKE.values()   # All values
SASUKE.items()    # All key-value pairs
# SASUKE.clear()  # Empties the dictionary


# Now, Lets Dive into the LOOPS

for i in [0, 1, 2, 3, 4, 5]:
    print(i)

for i in range(7):
    print(i)

for name in names:
    print(name)

for student in students:
    print(student)

name = "TAIMOOOOOOOOR"
for char in name:
    print(char)

for key in SASUKE:
    print(key, "->", SASUKE[key])

for key, value in SASUKE.items():
    print(f"{key}: {value}")