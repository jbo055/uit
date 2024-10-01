import tkinter as tk

root = tk.Tk()
root.geometry("300x400")
root.title("Lister Meny")
root.config(bg="#F6A9A2")

main_frame = tk.Frame(root, bg="#F6A9A2")
main_frame.place(x=0, y=0, width=300, height=400)

header_label = tk.Label(
    main_frame,
    text="Lister Meny",
    font=("rustic barn", 24),
    bg="#F6A9A2",
    relief=tk.RAISED
)
header_label.place(
    x=10,
    y=10,
    width=251,
    height=50
)

people_list = []
file_path = "People.txt"

def write_person_to_file(person):
    with open(file_path, 'a') as file:
        file.write(f"{person}\n")

def load_people_from_file():
    try:
        with open(file_path, 'r') as file:
            for line in file:
                person = line.strip()
                people_list.append(person)
    except FileNotFoundError:
        print(f"{file_path} not found. Starting with an empty list.")

def return_to_main_menu():
    pass

def main_menu():
    pass

def open_people_list():
    for widget in main_frame.winfo_children():
        widget.destroy()
    open_list_menu()

def open_list_menu():
    header_label_openlist = tk.Label(
        main_frame,
        text="Din liste",
        font=("rustic barn", 24),
        bg="#F6A9A2",
        relief=tk.RAISED
    )
    header_label_openlist.place(
        x=10,
        y=10,
        width=251,
        height=50
    )
    
    global people_listbox
    people_listbox = tk.Listbox(
        main_frame, 
        width=41, 
        height=14
    )
    people_listbox.place(
        x=10, 
        y=70
    )
    
    for person in people_list:
        people_listbox.insert(tk.END, person)
    
    entry = tk.Entry(main_frame, width=30)
    entry.place(x=10, y=250)
    
    def add_person():
        person = entry.get()
        if person:
            people_list.append(person)
            people_listbox.insert(tk.END, person)
            write_person_to_file(person)
            entry.delete(0, tk.END)
    
    add_button = tk.Button(
        main_frame,
        text="Legg til",
        font=("Helvetica", 12),
        bg="#F6A9A2",
        relief=tk.RAISED,
        command=add_person
    )
    add_button.place(
        x=10,
        y=280,
        width=251,
        height=30
    )
    
    return_button = tk.Button(
        main_frame,
        text="Tilbake",
        font=("Helvetica", 12),
        bg="#F6A9A2",
        relief=tk.RAISED,
        command=main_menu
    )
    return_button.place(
        x=10,
        y=310,
        width=251,
        height=50
    )

open_list_button = tk.Button(
    main_frame,
    text="Åpne liste",
    font=("Helvetica", 12),
    bg="#F6A9A2",
    relief=tk.RAISED,
    command=open_people_list
)
open_list_button.place(
    x=10,
    y=70,
    width=251,
    height=50
)

# Load values from file on startup
load_people_from_file()

root.mainloop()