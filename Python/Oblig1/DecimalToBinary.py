# Write a program that converts a decimal number to binary number.

# Prompt the user to enter a decimal number
num = int(input("Enter a decimal number between 0 and 15: "))

# Convert the decimal number to binary number
binary = bin(num)

# Check if num is between 0 and 15
if num < 0 or num > 15:
    print("You must enter a number between 0 and 15")
else:
    print(f"The binary representation of {num} is {binary[2:]}") # Remove the first two characters from the binary representation