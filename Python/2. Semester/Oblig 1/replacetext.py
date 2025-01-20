# Write a program that replaces text in a file. Your program should prompt the user to enter a filename, an old string, and a new string.

# Promt the user to enter a filename.
# Prompt the user to enter a filename.
import os
print("Current working directory:", os.getcwd())
def replace_text():
    filename = input("Enter the name of the file you would like to alter: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File content successfully read.")

        # Prompt the user to enter the old string.
        old_string = input("What string would you like to edit: ")

        # Prompt the user to enter the new string.
        new_string = input("What would you like to replace it with: ")

        # Replace the old string with the new string.
        new_content = content.replace(old_string, new_string)
        replacements = content.count(old_string)

        # Write the new content to the file.
        with open(filename, "w") as file:
            file.write(new_content)
            print(f"'{old_string}' was replaced {replacements} times with '{new_string}'.")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    replace_text()