# import csv
# import matplotlib.pyplot as plt
# from datetime import datetime


# filename = 'data/sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
    
#     # Get dates and high temperatures from this file
#     dates, highs = [], []

#     for row in reader:
#         current_date = datetime.strptime(row[2], '%Y-%m-%d')
#         high = int(row[5])
#         dates.append(current_date)
#         highs.append(high)

# # Plot the high temperatures.
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, c='red')

# # Format plot.
# plt.title("Daily high temperatures, July 2018", fontsize=24)
# ax.set_xlabel('Dates',fontsize=16)
# ax.set_ylabel('Temperature (F)', fontsize=16)
# fig.autofmt_xdate() # To formate date in automatic way
# plt.tick_params(axis='both', which='major', labelsize=16)

# plt.show()
# plt.set



#######################################################
# Ploting a longer timeframe

import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high temperatures from this file
    dates, highs = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures, 2018", fontsize=24)
ax.set_xlabel('Dates',fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
fig.autofmt_xdate() # To formate date in automatic way
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
plt.set
