# Write a program that prompts the user to enter the first 9 digits and displays the 10-digit ISBN (International Standard Book Number) number. 
# The ISBN-10 number is calculated as follows:
# (d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11
# If the checksum is 10, the last digit is denoted as X.
#

# Prompt the user to enter the first 9 digits of an ISBN number
num = input("Enter the first 9 digits of an ISBN number: ")

# Check if the number is exactly 9 digits
while len(num) != 9:
    print("Invalid input. Please enter exactly 9 digits.")
    num = input("Enter the first 9 digits of an ISBN number: ")
    if len(num) == 9:
        break

d1, d2, d3, d4, d5, d6, d7, d8, d9 = num
# print(d1, d2, d3, d4, d5, d6, d7, d8, d9)
checksum = (int(d1) * 1 + int(d2) * 2 + int(d3) * 3 + int(d4) * 4 + int(d5) * 5 + int(d6) * 6 + int(d7) * 7 + int(d8) * 8 + int(d9) * 9) % 11
# print(checksum)
if checksum == 10:
    print(f"The ISBN-10 number is {num}X")
else:
    print(f"The ISBN-10 number is {num}{checksum}")