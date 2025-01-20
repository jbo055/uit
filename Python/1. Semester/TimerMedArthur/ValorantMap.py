import folium
import folium.raster_layers
import pandas as pd
import webbrowser as wb

min_zoom_defined = 2.1
zoom_start_defined = 10
center = [0, 0]
bounds = [[-90, -180], [90, 180]]
f = folium.Figure(width=1000, height=500)
m = folium.Map(location= center, tiles="openstreetmap",
zoom_start=zoom_start_defined, min_zoom = min_zoom_defined).add_to(f)

f.save("test_map.html")
wb.open("test_map.html")

