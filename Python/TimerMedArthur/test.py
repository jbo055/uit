
#datatypes: 
#string - text
#str(int) - converts an integer to a string
#integer - whole number
#float - decimal number
#char - a single character
#boolean - true or false
#double - decimal number
#choice - a selection from a list of options


# print('*****************') #text is string
# print('welcome to my app')
# print('*****************')

# name = input('What is your name? ') #input is a variable, the name of the variable can be anything but it can not start with a number
# age = int(input('What is your age? ')) #converts the input to an integer (a whole number)
# print('Hello', name, '\nYou are', age, 'years old.') #name and age are variables that will be printed as strings in this case

# daysOld = age * 365 #multiplying the age by 365 to get the number of days old
# print('You are', daysOld, 'days old.') #printing the number of days old
# weight = float(input('What is your weight? ')) #converts the input to a float (a decimal number)

# letter = input('Enter a letter: ') #input a letter
# ASCII = ord(letter) #converts the letter to its ASCII value
# print('The ASCII value of', letter, 'is', ASCII) #prints the ASCII value of the letter

# pizzaAmount = int(input('How many pizzas do you want? ')) #input the number of pizzas
# pizzaCost = 10.00 #cost of a pizza
# totalCost = pizzaAmount * pizzaCost #calculating the total cost of the pizzas

# if pizzaAmount > 10:
#     print('That is too many pizzas!') #if the number of pizzas is greater than 10, print this
# elif pizzaAmount < 1:
#     print('That is too few pizzas!') #if the number of pizzas is less than 1, print this
# else: 
#     print('Great choice!')
#     print('That will be $', totalCost, '. Cash or card?') #printing the total cost of the pizzas

cokePrice = 2.00 #price of a coke
spritePrice = 2.50 #price of a sprite
# cokePrice = float(cokePrice) #converts the price of a coke to a float (a decimal number)
# spritePrice = float(spritePrice) #converts the price of a sprite to a float (a decimal number)



# choice = input('Do you want to order a drink? yes or no') #input if the user wants to order a drink

# while True:
#     if choice == 'yes' 
#         break
#     else:
#         print('Invalid input!')
#         choice = input('Do you want to order a drink? yes or no')


# if choice == 'yes': #if the user input is 'yes'
#     print('Great!') #print this
#     choiceDrink = input('Do you want a coke or a sprite? ') #input if the user wants a coke or a sprite
#     if choiceDrink == 'coke':
#         print('You ordered a coke.')
#         print('That will be $', cokePrice, '. Cash or card?') #if the user input is 'coke', print this
#     elif choiceDrink == 'sprite':
#         print('You ordered a sprite.')
#         print('That will be $', spritePrice, '. Cash or card?')
#     else:
#         print('Invalid input!')
# elif choice == 'no':
#     print('Okay!') #if the user input is 'no', print this
# else: 
#     print('Invalid input!')

choice = input('What would you like to order? \nYou can choose between food or drinks. Exit if you would like to leave.\n') #input what the user wants to order

while True:
    choice = input('What would you like to order? \nYou can choose between food or drinks. Exit if you would like to leave.\n') #input what the user wants to order
    while True:   
        if choice == 'food':
            foodOrder = input('Do you want a burger or a hotdog? ')
            if foodOrder == 'burger':
                print('You ordered a burger.')
                break
            elif foodOrder == 'hotdog':
                print('You ordered a hotdog.')
                break
            else:
                print('Invalid input!')
                break

        elif choice == 'drinks':
            drinkOrder = input('Do you want a coke or a sprite? ')
            if drinkOrder == 'coke':
                print('You ordered a coke.')
                break
            elif drinkOrder == 'sprite':
                print('You ordered a sprite.')
                break
            else:
                print('Invalid input!')
                break

        elif choice == 'exit':
            print('Goodbye!')
            break