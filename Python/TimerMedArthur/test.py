
#datatypes: 
#string - text
#str(int) - converts an integer to a string
#integer - whole number
#float - decimal number
#char - a single character

print('*****************') #text is string
print('welcome to my app')
print('*****************')

name = input('What is your name? ') #input is a variable, the name of the variable can be anything but it can not start with a number
age = int(input('What is your age? ')) #converts the input to an integer (a whole number)
print('Hello', name, '\nYou are', age, 'years old.') #name and age are variables that will be printed as strings in this case

daysOld = age * 365 #multiplying the age by 365 to get the number of days old
print('You are', daysOld, 'days old.') #printing the number of days old
weight = float(input('What is your weight? ')) #converts the input to a float (a decimal number)

letter = input('Enter a letter: ') #input a letter
ASCII = ord(letter) #converts the letter to its ASCII value
print('The ASCII value of', letter, 'is', ASCII) #prints the ASCII value of the letter

