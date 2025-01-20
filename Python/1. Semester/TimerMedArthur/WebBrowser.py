import tkinter as tk
import webbrowser as wb

root = tk.Tk()
root.geometry("300x400")
root.title("Web Browser")

def open_website():
    print("Open Website")
    url = text_field.get()
    wb.open(url)

def open_google_maps():
    print("Open Google Maps")
    lat = latitude_field.get()
    lon = longitude_field.get()
    wb.open(f"https://www.google.com/maps/@{lat},{lon},10z")
    

text_field = tk.Entry(root, width = 20)
text_field.pack(pady=5)

open_browser_button = tk.Button(root, text="Open Website", command = lambda: [open_website(), text_field.delete(0, tk.END)])
open_browser_button.pack(pady=5)

latitude_field_label = tk.Label(root, text = "Latitude")
latitude_field_label.pack(pady=5)

latitude_field = tk.Entry(root, width = 20)
latitude_field.pack(pady=5)

longitude_field_label = tk.Label(root, text = "Longitude")
longitude_field_label.pack(pady=5)

longitude_field = tk.Entry(root, width = 20)
longitude_field.pack(pady=5)

open_maps_button = tk.Button(root, text="Open Map", command = lambda: [open_google_maps(), text_field.delete(0, tk.END)])
open_maps_button.pack(pady=5)


root.mainloop()