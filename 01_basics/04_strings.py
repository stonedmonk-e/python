# 'hello' is the same as "hello"

# strings are arrays, they can be indexed
a = "Hello Bro"
print(a[1]) # e

# finding length
print(len(a))

# looping
for x in "banana" :
    print(x)

# to check if certain phrase or char is present in a string, 
# we can use keyword "in"
txt = "India will win next world cup"
print("next" in txt) # True

# there's also a "not in" keyword
txt = "India will win next world cup"
if "this" not in txt:
    print("No") # No

# ------------------------------------------------------------ #

# slicing
# to return the characters in specified range, last digit not included
b = "Hello paapu"
print(b[2:7]) # llo p => p is at 6th index

# slice from start
print(b[:7]) # Hello p

# slice to end
print(b[2:]) # llo paapu

# negative indexing => to start slicing from end of string
print(b[-7:-2]) # o paa

# ------------------------------------------------------------ #

# Modify strings
x = "I love PythON   " # => has whitespaces at end

print(x.upper())
print(x.lower())

# The strip() method removes any whitespace from the beginning or the end
print(x.strip()) 

# replaces a char or string
print(x.replace("love", "hate")) # I hate PythON

# split() => spilts strings into substrings if it finds separator
# let's give whitespace " " as separator for x
print(x.split(" ")) # ['I', 'love', 'PythON', '', '', ''] => at end we have 3 whitespaces


# String concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c) # Hello World

# ------------------------------------------------------------ #

# Format
# to combine strings and numbers using format() method 
# it takes the passed arguments, formats them, and places them in the string where the placeholders {} are

quantity = 3
itemno = 878
price = 69.99
myorder = "I want {} pieces of item {} for {} rupees"
print(myorder.format(quantity, itemno, price)) # I want 3 pieces of item 878 for 69.99 rupees

# we can index the arguments too in placeholder
myorder = "I want to pay {2} rupees for {0} pieces of item {1} "
print(myorder.format(quantity, itemno, price)) # I want to pay 69.99 rupees for 3 pieces of item 878

# ------------------------------------------------------------ #

# Escape characters
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."

txt = "We are the so-called \"Vikings\" from the north." # We are the so-called "Vikings" from the north.
print(txt)

# Code	Result
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# ------------------------------------------------------------ #
