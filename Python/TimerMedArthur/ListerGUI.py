import tkinter as tk

root = tk.Tk()
root.geometry("300x400")
root.title("Lister Meny")
root.config(
    bg = "#F5978F"
    )

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
        text = "Lister Meny",
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
    
    list = []
    try:
        with open("ListerGUI.txt", "+r") as file:
            list = file.readlines()
            list = [item.strip() for item in list]  # Remove any extra whitespace or newline characters
    except FileNotFoundError:
        print("ListerGUI.txt not found. Starting with an empty list.")
    def write_list_to_file():
        with open("ListerGUI.txt", "+r") as file:
            for item in list:
                file.write(f"{item}\n")

    def open_list():
        for widget in main_frame.winfo_children():
            widget.destroy()
        open_list_menu()

    def open_list_menu():
        header_label_openlist = tk.Label(
        main_frame,
        text = "Din liste",
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
        listbox = tk.Listbox(
            main_frame, 
            width = 41, 
            height = 14
            )
        listbox.place(
            x = 10, 
            y = 70)
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
        

    def add_list():
        for widget in main_frame.winfo_children():
            widget.destroy()
        add_list_menu()

    def add_list_menu():
        header_label_addlist = tk.Label(
        main_frame,
        text = "Din liste",
        font = ("rustic barn", 24),
        bg = "#F6A9A2",
        relief = tk.RAISED
        )
        header_label_addlist.place(
            x = 10,
            y = 10,
            width = 251,
            height = 50
        )
        add_to_list = tk.Entry(
            main_frame, 
            width = 41)
        add_to_list.place(
            x = 10, 
            y = 70)
        add_button = tk.Button(
            main_frame,
            text = "Legg til",
            font = ("Helvetica", 12),
            bg = "#F6A9A2",
            relief = tk.RAISED,
            command = lambda: [list.append(add_to_list.get()), add_to_list.delete(0, tk.END)]
        )
        add_button.place(
            x = 10,
            y = 100,
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
        

    # def search_list():

    # def delete_list():

    # def update_list():

    open_list_button = tk.Button(
        main_frame,
        text = "Åpne liste",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        relief = tk.RAISED,
        command = open_list
    )
    open_list_button.place(
        x = 10,
        y = 70,
        width = 251,
        height = 50
    )

    add_list_button = tk.Button(
        main_frame,
        text = "Legg til liste",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        relief = tk.RAISED,
        command = lambda: [add_list(), write_list_to_file()]
    )
    add_list_button.place(
        x = 10,
        y = 130,
        width = 251,
        height = 50
    )

    search_list_button = tk.Button(
        main_frame,
        text = "Søk i liste",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        relief = tk.RAISED,
        # command = search_list
    )
    search_list_button.place(
        x = 10,
        y = 190,
        width = 251,
        height = 50
    )

    delete_list_button = tk.Button(
        main_frame,
        text = "Slett liste",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        relief = tk.RAISED,
        # command = delete_list
    )
    delete_list_button.place(
        x = 10,
        y = 250,
        width = 251,
        height = 50
    )

    update_list_button = tk.Button(
        main_frame,
        text = "Oppdater liste",
        font = ("Helvetica", 12),
        bg = "#F6A9A2",
        relief = tk.RAISED,
        # command = update_list
    )
    update_list_button.place(
        x = 10,
        y = 310,
        width = 251,
        height = 50
    )




        
    

main_menu()
root.mainloop()
