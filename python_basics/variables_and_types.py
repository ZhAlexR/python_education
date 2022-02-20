# Numbers
"""" The module contains exercise for task 2"""

my_int = 7
print(my_int)

my_float = 7.1
print(my_float)
my_float = float(5)

# Strings
my_string = "hello, World!"
print(my_string)

mystring_ = "Don't worry about apostrophes"
print(mystring_)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + ", " + world
print(helloworld)

a, b = 3, 4
print(a, b)

# This will not work! But if I use f-string, it will
one = 1
two = 2
hello = "hello"

print(f"{one} + {two} + {hello}")

# Exercise
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print(f"String: {mystring}")
if isinstance(myfloat, float) and myfloat == 10.0:
    print(f"Float: {myfloat}")
if isinstance(myint, int) and myint == 20:
    print(f"Integer: {myint}")
