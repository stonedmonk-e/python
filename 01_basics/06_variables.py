print("Hello, World!")

# The number of spaces is up to you as a programmer, 
# the most common use is four, but it has to be at least one

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

# You have to use the same number of spaces in the same block of code, 
# otherwise Python will give you an error:
# Syntax Error:

""" => this is multiline string, another way to comment
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
"""

# Variables are containers for storing data values. Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it, we can change the type later too

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
# Casting is done using constructor functions => int(), float(), str()

x1 = str(3)   # '3'
x2 = str("s1") # 's1'
x3 = str(3.0) # 3.0

y1 = int(4)   # 3
y2 = int(2.8) # 2
y3 = int("69") # 69

z1 = float(3) # 3.0
z2 = float("4.56") # 4.56
z3 = float("3") # 3.0

# String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

# Variable names are case-sensitive. This will create two variables:

a = 4
A = "Sally"
#A will not overwrite a

# Rules for variable names:
#     A variable name must start with a letter or the underscore character
#     A variable name cannot start with a number
#     A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#     Variable names are case-sensitive (age, Age and AGE are three different variables)
#     A variable name cannot be any of the Python keywords.


# examples of illegal names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

"""
For multiword variable names:
Camel Case: Each word, except the first, starts with a capital letter:
    myVariableName = "John"

Pascal Case: Each word starts with a capital letter:
    MyVariableName = "John"

Snake Case: Each word is separated by an underscore character:
    my_variable_name = "John"

"""

# Assigning multiple values to multiple variables at once
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# assigning one value to multiple variables at once
x = y = z = 122
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. 
# Python allows you to extract the values into variables. This is called unpacking.
# Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits   # make sure you're extracting all of them
print(x)
print(y)
print(z)


# Output variables
# print can be used to output multiple variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x+y+z)

#different data types
a = 5
# print(a+z) => cannot be done, so use comma
print(a, z); #5 awesome


# Global Variables

x = "awesome"

def myfunc():
    x = "fantastic"
    print("python is "+x) # python is fantastic

myfunc()

print("Python is "+x) # Python is awesome

# To change the value of a global variable inside a function,
# refer to the variable by using the global keyword:
def myfunc():
  global x
  x = "fantastic"
