# strings
name = "WinnY the POOh"

# uppercase and lowercase
print(name.upper()) # WINNY THE POOH
print(name.lower()) # winny the pooh

# indexing from 0

# Find function
print(name.find('P')) # 10
print(name.find('r')) # doesn't exist so -1
print(name.find(' ')) # 5

# replace function
print(name.replace("WinnY", "Johnny"))  # Johnny the POOh
print(name.replace("PO", "R"))  # WinnY the ROh

# check for substring in string
print("W" in name) # True
print("POOh" in name) # True
print("U" in name) # False

