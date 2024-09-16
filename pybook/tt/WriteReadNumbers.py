from random import randint 

def main():
    # Open file for writing data
    output = open("Numbers.txt", "w")
    for i in range(10):
        output.write(str(randint(0, 9)) + " ")
    output.close() # Close the file

    # Open file for reading data
    input = open("Numbers.txt", "r")
    s = input.read() # Read all data to s
    numbers = [float(x) for x in s.split()]
    for number in numbers:
        print(number, end = " ")
    input.close() # Close the file
    
main() # Call the main function
