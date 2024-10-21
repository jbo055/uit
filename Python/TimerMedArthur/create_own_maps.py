import tkinter as tk
import webbrowser as wb
import folium
import pandas as pd
import tkinter.filedialog as filedialog
from folium.plugins import HeatMap



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
    
def open_excel():
    print("Open Excel")
    filepath = filedialog.askopenfilename()
    file = pd.read_excel(filepath)
    display_map(file)

    
def display_map(file):
    print("Display Map")
    center = [47.322, 10.535]
    new_map = folium.Map(center, zoom_start = 10)

    #i want to use the info in the excel file
    for i, row in file.iterrows():
        folium.Marker([row["latitude"], row["longitude"]], popup = row["location"]).add(new_map)

    new_map.save("test_map.html")
    wb.open("test_map.html")

make_map_button = tk.Button(root, text="Make Map", command = lambda: [display_map(), text_field.delete(0, tk.END)])
make_map_button.pack(pady=5)

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

open_excel_button = tk.Button(root, text="Open Excel", command = lambda: [open_excel(), text_field.delete(0, tk.END)])
open_excel_button.pack(pady=5)


root.mainloop()