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

#open menu

# def open_menu():





root.mainloop()

