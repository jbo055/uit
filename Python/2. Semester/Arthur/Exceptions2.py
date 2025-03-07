import os

def open_file():
    with open("test.txt", "r") as file: # This is a very important keyword to connect to files, or databases, or webservices, etc.
        try:
            file.read()
        except Exception as e:
            print(f"An error occurred: {e}")
        except FileNotFoundError:
            print(f"The file was not found. {e}")
        else:
            file.close()

def open_file_v2():
    with open("test.txt", "r") as file: # file pointer - file handling
        content = file.read()
        print(content)

def write_to_file():
    with open("test.txt", "w") as file:
        test = "Test string"
        file.write(test)

        file.flush() # Garbage collection

        file.close()

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()