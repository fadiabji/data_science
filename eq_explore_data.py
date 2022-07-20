import json

#Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file,'w') as f:
#     json.dump(all_eq_data, f, indent=4)

metadata_eq= all_eq_data['metadata']
print(metadata_eq)

# How many Earthquakes were happened the last 24 houres:
all_eq_data = all_eq_data['features']
print(len(all_eq_data))

# extracting Magnitudes:
mags = []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
print(mags[:10])

# Extracting Location Data:
lons, lats = [], []
for eq_dict in all_eq_data:
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)
print(lons[:10])
print(lats[:10])
