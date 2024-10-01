import tkinter as tk

values_list = []  # This is a list, and it is a global variable.

def add_value():  # This is a function and not a method.
    value = entry.get()
    values_list.append(value)
    print("new value in list:", str(value))
    values_listbox.insert(tk.END, value)

def print_to_file():
    try:
        with open("ListerGUI.txt", "+r") as file:
            for item in values_list:
                file.write(f"{item}\n")
    except FileNotFoundError:
        print("ListerGUI.txt not found. Starting with an empty list.")
        with open("ListerGUI.txt", "+w") as file:
            for item in values_list:
                file.write(f"{item}\n")

def load_values_from_file():
    try:
        with open("ListerGUI.txt", "r") as file:
            for line in file:
                value = line.strip()
                values_list.append(value)
                values_listbox.insert(tk.END, value)
    except FileNotFoundError:
        print("ListerGUI.txt not found. Starting with an empty list.")

root = tk.Tk()  # TK is not only a function, it is called a method, and it is a method of the class Tk
root.title("GUI no. 2")
root.geometry("300x400")

# Making a label
label = tk.Label(root, text="Input Value")
label.place(x=10, y=30)

entry = tk.Entry(root, width=20)
entry.place(x=90, y=30)

submit_button = tk.Button(root, text="Submit", command=lambda: [add_value(), print_to_file(), entry.delete(0, tk.END)])
submit_button.place(x=200, y=60)

values_listbox = tk.Listbox(root, width=40, height=15)
values_listbox.place(x=10, y=100)

# Load values from file on startup
load_values_from_file()

root.mainloop()
