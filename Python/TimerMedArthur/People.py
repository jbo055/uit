import tkinter as tk
root = tk.Tk()
root.geometry("300x400")
root.title("People")
root.config(bg="#F6A9A2")

def main():
    

    main_frame = tk.Frame(root, bg="#F5978F", bd=5, relief=tk.SUNKEN)
    main_frame.place(x=10, y=10, width=280, height=380)

    header_label = tk.Label(main_frame, text="Favorite People", font=("rustic barn", 24), bg="#F6A9A2", relief=tk.RAISED)
    header_label.place(x=10, y=10, width=251, height=50)

    try:
        with open("People.txt", "r") as file:
            people = file.readlines()
            people = [item.strip() for item in people]  # Remove any extra whitespace or newline characters
    except FileNotFoundError:
        print("ListerGUI.txt not found. Starting with an empty list.")
        people = []

    def open_people_list_click():
        for widget in main_frame.winfo_children():
            widget.destroy()
        open_people_list()
    def open_people_list():
        header_label_openpeople = tk.Label(
            main_frame,
            text="People",
            font=("rustic barn", 24),
            bg="#F6A9A2",
            relief=tk.RAISED
        )
        header_label_openpeople.place(
            x=10,
            y=10,
            width=251,
            height=50
        )

        global people_listbox
        people_listbox = tk.Listbox(
            main_frame,
            width=41,
            height=14,
            bg="#F6A9A2",
            relief=tk.SUNKEN,
            bd = 1
        )
        people_listbox.place(x=10, y=70)

        for item in people:
            people_listbox.insert(tk.END, item)

        return_button = tk.Button(
        main_frame,
        text = "Return",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        activebackground = "#F6A9A2",
        relief = tk.RAISED,
        command = main
        )
        return_button.place(
            x = 10,
            y = 310,
            width = 251,
            height = 50
            )

    open_list_button = tk.Button(
        main_frame,
        text = "See people",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        activebackground = "#F6A9A2",
        relief = tk.RAISED,
        command = open_people_list_click
        )
    open_list_button.place(
        x = 10,
        y = 70,
        width = 251,
        height = 50
        )

    def add_people_click():
        for widget in main_frame.winfo_children():
            widget.destroy()
        add_people()
    def add_people():
        header_label_addpeople = tk.Label(
            main_frame,
            text="Add People",
            font=("rustic barn", 24),
            bg="#F6A9A2",
            relief=tk.RAISED
        )
        header_label_addpeople.place(
            x=10,
            y=10,
            width=251,
            height=50
        )

        global add_people_entry
        add_people_entry = tk.Entry(
            main_frame,
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            relief = tk.SUNKEN,
            bd = 5
        )
        add_people_entry.place(
            x = 10,
            y = 70,
            width = 251,
            height = 30
        )

        def add_people_to_list():
            new_person = add_people_entry.get()
            people.append(new_person)
            people_listbox.insert(tk.END, new_person)
            add_people_entry.delete(0, tk.END)
            with open("People.txt", "a") as file:
                file.write(f"{new_person}\n")

        add_people_button = tk.Button(
            main_frame,
            text = "Add Person",
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            activebackground = "#F6A9A2",
            relief = tk.RAISED,
            command = add_people_to_list
        )
        add_people_button.place(
            x=10,
            y=110,
            width=251,
            height=50
        )

        return_button = tk.Button(
            main_frame,
            text="Return",
            font=("Helvetica", 12),
            bg="#F6A9A2",
            activebackground="#F6A9A2",
            relief=tk.RAISED,
            command=main
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
        activebackground = "#F6A9A2",
        relief = tk.RAISED,
        command = add_people_click
        )
    add_people_button.place(
        x = 10,
        y = 130,
        width = 251,
        height = 50
        )

    def search_people():
        for widget in main_frame.winfo_children():
            widget.destroy()
        search_people_menu()
    def search_people_menu():
        main_frame = tk.Frame(
            root, 
            bg="#F5978F", 
            bd=5, 
            relief=tk.SUNKEN
            )
        main_frame.place(
            x = 10, 
            y = 10, 
            width = 280, 
            height = 380
            )
        
        header_label_searchpeople = tk.Label(
            main_frame,
            text = "Search People",
            font = ("rustic barn", 24),
            bg = "#F6A9A2",
            relief = tk.RAISED
            )
        header_label_searchpeople.place(
            x = 10,
            y = 10,
            width = 251,
            height = 50
            )
        
        search_entry = tk.Entry(
            main_frame,
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            relief = tk.SUNKEN,
            bd = 5
            )
        search_entry.place(
            x = 10,
            y = 70,
            width = 251,
            height = 30
            )
        search_result_label = tk.Label(
            main_frame,
            text = "",
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            relief = tk.SUNKEN,
            bd = 5
            )
        search_result_label.place(
            x = 10,
            y = 170,
            width = 251,
            height = 50
            )
        
        
        def search_people():
            search_term = search_entry.get()
            if search_term in people:
                search_result = f"{search_term} is in the list."
            else:
                search_result = f"{search_term} is not in the list."
            search_entry.delete(0, tk.END)
            search_result_label.config(text = search_result)

        search_button = tk.Button(
            main_frame,
            text = "Search",
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            activebackground = "#F6A9A2",
            relief = tk.RAISED,
            command = search_people
        )
        search_button.place(
            x=10,
            y=110,
            width=251,
            height=50
        )
        
        return_button = tk.Button(
            main_frame,
            text="Return",
            font=("Helvetica", 12),
            bg="#F6A9A2",
            activebackground="#F6A9A2",
            relief=tk.RAISED,
            command=main
            )
        return_button.place(
            x = 10,
            y = 310,
            width = 251,
            height = 50
            )

    search_people_button = tk.Button(
        main_frame,
        text = "Search for someone",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        activebackground = "#F6A9A2",
        relief = tk.RAISED,
        command = search_people
        )
    search_people_button.place(
        x = 10,
        y = 190,
        width = 251,
        height = 50
        )

    def delete_people():
        for widget in main_frame.winfo_children():
            widget.destroy()
        delete_people_menu()
    def delete_people_menu():
        header_label_deletepeople = tk.Label(
            main_frame,
            text = "Delete People",
            font = ("rustic barn", 24),
            bg = "#F6A9A2",
            relief = tk.RAISED
            )
        header_label_deletepeople.place(
            x = 10,
            y = 10,
            width = 251,
            height = 50
            )
        
        global delete_people_entry
        delete_people_entry = tk.Entry(
            main_frame,
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            relief = tk.SUNKEN,
            bd = 5
            )
        delete_people_entry.place(
            x = 10,
            y = 70,
            width = 251,
            height = 30
            )
        
        def delete_people_from_list():
            delete_person = delete_people_entry.get()
            if delete_person in people:
                people.remove(delete_person)
                with open("People.txt", "w") as file:
                    for person in people:
                        file.write(f"{person}\n")
            delete_people_entry.delete(0, tk.END)

        delete_people_button = tk.Button(
            main_frame,
            text = "Delete Person",
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            activebackground = "#F6A9A2",
            relief = tk.RAISED,
            command = delete_people_from_list
            )
        delete_people_button.place(
            x = 10,
            y = 110,
            width = 251,
            height = 50
            )
        
        return_button = tk.Button(
            main_frame,
            text="Return",
            font=("Helvetica", 12),
            bg="#F6A9A2",
            activebackground="#F6A9A2",
            relief=tk.RAISED,
            command=main
            )
        return_button.place(
            x = 10,
            y = 310,
            width = 251,
            height = 50
            )

    delete_people_button = tk.Button(
        main_frame,
        text = "Delete people",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        activebackground = "#F6A9A2",
        relief = tk.RAISED,
        command = delete_people
        )
    delete_people_button.place(
        x = 10,
        y = 250,
        width = 251,
        height = 50
        )

    

    

if __name__ == "__main__":
    main()
    
root.mainloop()