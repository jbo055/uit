# lag gui meny for å lagge til kunder og detaljer ved bruk av tkinter

import tkinter as tk

root = tk.Tk()
root.geometry("500x600")
root.title("Kunde App")
root.configure(bg = "#385F71")

# Label
# program_label_frame = tk.Frame(root, bg = "#2F5060")

program_label = tk.Label(
    root, 
    text = "Kunde App",  
    font = ("Helvetica", 20), 
    bg = "#2F5060", 
    fg = "black", 
    width = 10
)
program_label.place(x = 250, y = 50, anchor = "center")

# add a box with information and a get started button below the information

info_frame = tk.Frame(root, bg = "#2F5060", bd = 2)
info_frame.place(
    x = 250, 
    y = 300, 
    anchor = "center", 
    width = 300, 
    height = 350
    )
info_label = tk.Label(
    info_frame,
    text = "Velkommen til kundeappen!\n\nHer kan du administrere dine kunder\nenkelt",
    font = ("Helvetica", 12),
    bg = "#2F5060",
    fg = "white"
)
info_label.pack(pady = 10)

#start button
#function to get access to the other funtions of the program

def get_started():
    for widget in root.winfo_children():
        widget.destroy()
    open_menu()

def add_customer_click():
    for widget in root.winfo_children():
        widget.destroy()
    add_customer()    
def add_customer():
    print("add customer")

def open_menu():
    add_customer = tk.Button(
        root,
        text = "Ny kunde",
        font=("Helvetica", 12), 
        bg="white", 
        fg="black",
        command = add_customer_click
    )
    add_customer.pack(pady = 10)

    edit_customer = tk.Button(
        root,
        text="Rediger kunde",
        font=("Helvetica", 12), 
        bg="white", 
        fg="black"
    )
    edit_customer.pack(pady = 10)

    delete_customer = tk.Button(
        root,
        text = "Slett kunde",
        font=("Helvetica", 12), 
        bg="white", 
        fg="black"
    )
    delete_customer.pack(pady = 10)

    search_customer = tk.Button(
        root,
        text = "Søk etter kunde",
        font=("Helvetica", 12), 
        bg="white", 
        fg="black"
    )
    search_customer.pack(pady = 10)
    
get_started_button = tk.Button(
    info_frame, 
    text="Get Started", 
    font=("Helvetica", 20), 
    bg="white", 
    fg="black",
    command=get_started
)
get_started_button.pack(pady=100)


#open menu

# def open_menu():





root.mainloop()

