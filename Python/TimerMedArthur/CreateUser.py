#testing the functions in creation of user profiles.

def createUser():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    return name, age

def printUser(name, age):
    print(f'Your name is {name} and you are {age} years old.')

name, age = createUser()
printUser(name, age)

