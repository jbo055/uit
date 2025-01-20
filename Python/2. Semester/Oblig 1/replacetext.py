# Write a program that replaces text in a file. Your program should prompt the user to enter a filename, an old string, and a new string.

# Promt the user to enter a filename.
filename = input("Enter the name of the file you would like to alter: ")
file = open(filename, "+r")
content = file.read()
print(content)
