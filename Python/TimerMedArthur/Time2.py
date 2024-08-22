#can convert to a float in two lines, or in one line

# number1 = input("Enter the first number: ")
# number1 = float(number1)

#a void function is a function the doesnt have a return value
#make a function that will do this job for us. This is a good practice to make a function for repetitive tasks
def addNumber1and2(): #in those brackets we use our ingredients.
    #the function body
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = number1 + number2
    return result
#you will not see the function in use unless you use the function. Making the function is called function definition.
#Using the function is called function call.
# addNumber1and2() #this is a function call

# print(f'The sum of the two numbers is {addNumber1and2()}') #here you dont have to convert the variable result

# number1 = float(input("Enter the first number: "))

# number2 = float(input("Enter the second number: "))

# result = number1 + number2

# #two ways to print the result

# print("The sum of the two numbers is", str(result)) #this is easier to understand and more similar to C++ or Java or C#
# print(f'The sum of the two numbers is {result}') #here you dont have to convert the variable result

def voidFunctionExample():
    print("This is a void function.")
    print("It does not return a value.")
    print('I can\'t imagine actually needing to use this function.')
    print('It is just an example.')
    print('I guess maybe I could use it as a method to return a response to a user.')
    print('I could also use it to print a message to the console.')

# voidFunctionExample()

# in those brackets we use our ingredients.

def ingriedientFunction(num1, num2):
    result = num1 + num2
    print('The result is', str(result))
#this is still a void function, because it has no return value

# number1  = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))

# ingriedientFunction(number1, number2)

# ingriedientFunction(8, 32)
def recieveNumbers(number1, number2):
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    return number1, number2
def multiplyNumbers(num1, num2):
    result = num1 * num2
    return result
number1, number2 = recieveNumbers(0, 0) 
# print(f'The product of the two numbers is {multiplyNumbers(number1, number2)}')
sum = multiplyNumbers(number1, number2) #vi lagrer resultatet i en variabel
print(f'The product of the two numbers is {sum}') #her printer vi resultatet som vi har lagret




