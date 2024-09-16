def read_file():
    # filename =('test.txt')
    filename = input("Enter the name of the file you want to read: ")
    file = open(filename, "+r")
    content = file.read()
    print(content)

def write_file():
    filename = input("Enter the name of the file you want to write to: ")
    file = open(filename, "a+")
    text_to_add = input("Enter the text you want to add to the file: ")
    file.write(text_to_add+"\n")
    content = file.read()
    print(content)

def search_file():
    filename = input("Enter the name of the file you want to search: ")
    file = open(filename, "+r")
    search_term = input("Enter the term you want to search for: ")
    content = file.read()
    if search_term in content:
        print("The term was found in the file.")
    else:
        print("The term was not found in the file.")
    print(content)
    
# read a text file, write to a text file, search in a text file. 

def main_menu():
    choice = 0 
    while choice != 4:
        print("1. Read a text file. \n2. Write to a text file. \n3. Search in a text file. \n4. Exit.")
        choice = int(input("Pick your poison: "))

        if choice == 1:
            print("Reading file...")
            read_file()
        elif choice == 2:
            print("Writing to file...")
            write_file()
        elif choice == 3:
            print("Searching in file...")
            search_file()
        elif choice == 4:
            print("Exiting...")
        else:
            print("Invalid choice. Try again.")
    return

if __name__ == "__main__":
    main_menu()
