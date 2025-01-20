import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as matgraf


root = tk.Tk()
root.geometry("300x400")
root.title("Excel File")

def open_excel():
    # We want to open an excel file
    file_path = tk.filedialog.askopenfile()
    excel_file = pd.read_excel(file_path)

    x = excel_file[excel_file.columns[0]]
    y = excel_file[excel_file.columns[1]]

    print(x)
    print(y)

    fig, ax = plt.subplots()

    ax.set_title("Visualization")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    canvas = matgraf.FigureCanvasTkAgg(fig, master = root)
    canvas.get_tk_widget().pack(pady = 5)
    canvas.draw()

open_button = tk.Button(
    root,
    text = "Open Excel File",
    command = open_excel
)
open_button.pack(pady = 5)





root.mainloop()