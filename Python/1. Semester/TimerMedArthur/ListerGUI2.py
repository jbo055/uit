import tkinter as tk

root = tk.Tk()
root.geometry("300x400")
root.title("People")
root.config(
    bg = "#F5978F"
    )
people_list = []  # This is a list, and it is a global variable.



def main_menu():
    main_frame = tk.Frame(root, 
                        bg = "#F7B1AB",
                        bd = 5,
                        relief = tk.SUNKEN
                        )
    main_frame.place(
        x = 10,
        y = 10,
        width = 280,
        height = 380
    )

    header_label = tk.Label(
        main_frame,
        text = "People Menu",
        font = ("rustic barn", 24),
        bg = "#F6A9A2",
        relief = tk.RAISED
    )
    header_label.place(
        x = 10,
        y = 10,
        width = 251,
        height = 50
    )
    def open_people_list():
        for widget in main_frame.winfo_children():
            widget.destroy()
        open_people_list_menu()

    def open_people_list_menu():
        header_label_openlist = tk.Label(
            main_frame,
            text = "People list",
            font = ("rustic barn", 24),
            bg = "#F6A9A2",
            relief = tk.RAISED
        )
        header_label_openlist.place(
            x = 10,
            y = 10,
            width = 251,
            height = 50
        )

        global people_listbox
        people_listbox = tk.Listbox(
            main_frame,
            width = 41,
            height = 14
        )
        people_listbox.place(
            x = 10,
            y = 70
        )
        def load_people_from_file():
            try:
                with open("People.txt", "r") as file:
                    for line in file:
                        people = line.strip()
                        people_list.append(people)
                        people_listbox.insert(tk.END, people)
            except FileNotFoundError:
                print("People.txt not found. Starting with an empty list.")
        load_people_from_file()
        return_button = tk.Button(
            main_frame,
            text = "Tilbake",
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            relief = tk.RAISED,
            command = main_menu
        )
        return_button.place(
            x = 10,
            y = 310,
            width = 251,
            height = 50
        )
    
    open_list_button = tk.Button(
        main_frame,
        text = "Åpne liste",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        relief = tk.RAISED,
        command = open_people_list
    )
    open_list_button.place(
        x = 10,
        y = 70,
        width = 251,
        height = 50
    )
    def write_people_to_file():
            with open("People.txt", "w") as file:
                for person in people_list:
                    file.write(f"{people}\n")
    def add_people():
        for widget in main_frame.winfo_children():
            widget.destroy()
        add_people_menu()
    def add_people_menu():
        def add_people():
            new_people = new_people_entry.get()
            people_list.append(new_people)
            print("new people in list:", str(new_people))
            
        header_label_addpeople = tk.Label(
            main_frame,
            text = "Add people",
            font = ("rustic barn", 24),
            bg = "#F6A9A2",
            relief = tk.RAISED
        )
        header_label_addpeople.place(
            x = 10,
            y = 10,
            width = 251,
            height = 50
        )
        
        new_people_entry = tk.Entry(
            main_frame,
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            relief = tk.SUNKEN,
            bd = 5
        )
        new_people_entry.place(
            x = 10,
            y = 85,
            width = 251,
            height = 30
        )
        
        add_people_button = tk.Button(
            main_frame,
            text = "Add people",
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            relief = tk.RAISED,
            command = lambda: [add_people(), write_people_to_file(), add_people_menu()]
        )
        add_people_button.place(
            x = 10,
            y = 130,
            width = 251,
            height = 50
        )
        
        return_button = tk.Button(
            main_frame,
            text = "Tilbake",
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            relief = tk.RAISED,
            command = main_menu
        )
        return_button.place(
            x = 10,
            y = 310,
            width = 251,
            height = 50
        )

        
    
    add_people_button = tk.Button(
        main_frame,
        text = "Add people",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        relief = tk.RAISED,
        command = lambda: [add_people(), write_people_to_file(), add_people_menu()]
    )
    add_people_button.place(
        x = 10,
        y = 130,
        width = 251,
        height = 50
    )


main_menu()
root.mainloop()
