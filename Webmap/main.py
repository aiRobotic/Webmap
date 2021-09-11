import pandas as pd
import folium as fl

def draw_color (value):
    if value <1000.0:
        return "green"
    elif value>1000.0 and value<2000.0:
        return "orange"
    else:
        return "red"

df = pd.read_csv("Volcanoes.txt")
lat= list(df["LAT"])
lon= list(df["LON"])
height= list(df["ELEV"])


map = fl.Map(location =[lat[0],lon[0]], tiles = "cartodb positron")
fg = fl.FeatureGroup("my_map")
for lt, ln, hg in zip(lat,lon, height):
    fg.add_child(fl.Marker(location = [lt,ln], popup =hg, 
    icon = fl.Icon(color=draw_color(hg))))
map.add_child(fg)
map.save("MyMap.html")



