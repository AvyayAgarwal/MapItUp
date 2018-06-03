import folium
import pandas as pd
import requests
import io
import numpy as np
import math

data = requests.get("https://data.nasa.gov/resource/y77d-th95.csv").text
data = pd.read_csv(io.StringIO(data))

lat = list(data["reclat"])
lon = list(data["reclong"])
name = list(data["name"])
mass = list(data["mass"])
info = """<h4>Meteorite Info: </h4><p>Name: %s <br>Mass: %s</p>"""

map = folium.Map(location=[43.591991, -79.643306], zoom_start = 5, tiles="Mapbox Bright" )

fg = folium.FeatureGroup(name = "Meteorite Spots")

for x,y,n,m in zip(lat,lon,name,mass):
    iframe  = folium.IFrame(html=info % (str(n),str(m)), width=150,height=100)
    if math.isnan(x)==False and math.isnan(y)==False:
        fg.add_child(folium.CircleMarker(location=[x, y], popup=folium.Popup(iframe), radius=4, color='lightred', fill_color='red', fill_opacity = 0.5, fill = True))

map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("map.html")