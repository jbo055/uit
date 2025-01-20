# Prompt the user to enter a three-digit integer
num = int(input("Enter a three-digit integer: "))

# Check if the number is a palindrome
num = str(num)
if num == num[::-1]: # Check if the number is equal to its reverse
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")