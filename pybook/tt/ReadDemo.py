def main():
    # Open file for input
    input = open("Presidents.txt", "r")
    print("(1) Using read(): ")
    print(input.read()) # Read all in the file
    input.close() # Close the input file

    # Open file for input
    input = open("Presidents.txt", "r")
    print("\n(2) Using read(number): ")
    s1 = input.read(4) 
    print(s1)
    s2 = input.read(15) # Read 15 characters to s2
    print(repr(s2))
    input.close() # Close the input file

    # Open file for input
    input = open("Presidents.txt", "r")
    print("\n(3) Using readline(): ")
    line1 = input.readline() # Read a line
    line2 = input.readline()
    line3 = input.readline()
    line4 = input.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))
    input.close() # Close the input file

    # Open file for input
    input = open("Presidents.txt", "r")
    print("\n(4) Using readlines(): ")
    print(input.readlines())
    input.close() # Close the input file

main() # Call the main function
