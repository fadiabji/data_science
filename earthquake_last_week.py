import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/1.0_week.json'
with open(filename) as f:
    all_eq_data = json.load(f)


data_title = all_eq_data['metadata']['title']

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
print(mags[:10])
print(lons[:10])
print(lats[:10])



#Map the earthquakes. 
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text': hover_texts,
    'marker':{
    'size':[2*mag for mag in mags]
,    'color':mags,
    'colorscale':'Hot',
    'reversescale': True,
    'colorbar':{'title':'Magnitude'},
    }
}]# this is another way to define the data and will work good with plotly

my_layout = Layout(title=data_title)

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')


