import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file,'w') as f:
#     json.dump(all_eq_data, f, indent=4)

# metadata_eq= all_eq_data['metadata']
# print(metadata_eq)

# How many Earthquakes were happened the last 24 houres:
all_eq_data = all_eq_data['features']
print(len(all_eq_data))

# Extracting  Magnitudes and Location Data:
mags, lons, lats, hover_texts= [], [], [], []
for eq_dict in all_eq_data:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes. 
# Data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text': hover_texts,
    'marker':{
    'size':[2*mag for mag in mags],
    'color':mags,
    'colorscale':'Hot',
    'reversescale': True,
    'colorbar':{'title':'Magnitude'},
    }
}]# This is another way to define the data and will work good with plotly

my_layout = Layout(title='Global Earthquakes')
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')
