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


fg_population = fl.FeatureGroup("my_population")
fg_population.add_child(fl.GeoJson(data = open('world.json','r',encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005']< 10000000 else 'orange' if 10000000< x['properties']['POP2005'] < 20000000 else 'red'}))

layer_control = fl.LayerControl(position ='topright')

map.add_child(fg)
map.add_child(fg_population)
map.add_child(layer_control)

map.save("MyMap.html")



