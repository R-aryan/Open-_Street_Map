import folium
import pandas as pd

map= folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

fg= folium.FeatureGroup(name='My map')


data = pd.read_csv("Volcanoes.txt")
#print(data)
latitude= list(data['LAT'])
longitude= list(data['LON'])

for lt,ln in zip(latitude,longitude):
    fg.add_child(folium.Marker(location=[lt,ln],popup="Hi I am marker",icon=folium.Icon(color='green')))

map.add_child(fg)


map.save("Map1.html")

print("running Successfully")
