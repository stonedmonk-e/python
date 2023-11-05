first = input("Enter first number: ")
second = input("Enter second number: ")

sum = first + second
print(sum) # 57
# because it concatenates as strings

sum = int(first) + int(second)
print(sum)

print("the sum is: " + str(sum)) # here we convert coz concatenation error come

