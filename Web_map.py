import folium

map= folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

fg= folium.FeatureGroup(name='My map')

fg.add_child(folium.Marker(location=[38.2,-99.09],popup="Hi I am marker",icon=folium.Icon(color='green')))
map.add_child(fg)



map.save("Map1.html")

print("running Successfully")
