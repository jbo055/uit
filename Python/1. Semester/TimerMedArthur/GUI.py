# GUI -> Graphical User Interface

import tkinter as tk

root = tk.Tk()
root.geometry("300x400")
root.title("Julie sin App")

# Button

# def button_click_stein():
#     print("Stein")
#     stein["text"] = "Du valgte stein"

# def button_click_saks():
#     print("Saks")
#     saks["text"] = "Du valgte saks"

# def button_click_papir():
#     print("Papir")
#     papir["text"] = "Du valgte papir"


# stein = tk.Button(root, text = "Stein", command = button_click_stein, font = ("Helvetica", 14))
# stein.pack(pady = 15)

# saks = tk.Button(root, text = "Saks", command = button_click_saks, font = ("Helvetica", 14))
# saks.pack(pady = 15)

# papir = tk.Button(root, text = "Papir", command = button_click_papir, font = ("Helvetica", 14))
# papir.pack(pady = 15)


counter = 0
def counter_button_click():
    global counter # declaring the variable as global
    counter = counter + 1 # this will not work alone, we need to add the global counter
    counter_label["text"] = f"Counter: {counter}"

counter_button = tk.Button(root, text = "Counter", command = counter_button_click, font = ("Helvetica", 14))
counter_button.pack(pady = 15)

counter_label = tk.Label(root, text = "Counter: 0", font = ("Helvetica", 14))
counter_label.pack(pady = 15)

# def do_not_press():
#     print("I told you not to press it!")
#     counter_button["text"] = "I told you not to press it!"
#     counter_button["bg"] = "red"
#     counter_button["fg"] = "white"
# counter_button = tk.Button(root, text = "Do Not Press", command = do_not_press, font = ("Helvetica", 14))
# counter_button.pack(pady = 15)

root.mainloop()