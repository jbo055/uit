import os.path
import sys

def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter a target file: ").strip()

    # Check if target file exists
    if os.path.isfile(f2):
        print(f2 + " already exists")
        sys.exit()

    # Open files for input and output
    input = open(f1, "r")
    output = open(f2, "w")

    # Copy from input file to output file
    countLines = countChars = 0
    for line in input:
        countLines += 1
        countChars += len(line)
        output.write(line) # Write line to output
    print(countLines, "lines and", countChars, "chars copied")

    input.close()  # Close the input file
    output.close() # Close the output file

main() # Call the main function
