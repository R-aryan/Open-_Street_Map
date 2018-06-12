import folium
import pandas as pd

map= folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

fg= folium.FeatureGroup(name='My map')


data = pd.read_csv("Volcanoes.txt")
#print(data)
latitude= list(data['LAT'])
longitude= list(data['LON'])
elev=list(data['ELEV'])

def color_produce(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lt,ln ,el in zip(latitude,longitude,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(str(el)+" mtr",parse_html=True),
                               fill_color=color_produce(el),fill= True ,color='grey',fill_capacity=0.7))
    
#points for locations
#lines for lines
#polygons for areas

fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(folium.LayerControl())


map.save("Map1.html")

print("running Successfully")
