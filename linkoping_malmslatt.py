import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/malmslätt_Linkoping_weather_dataset.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)


    #Get dates, high and low temperatures from this file.
    dates, highs, lows = [], [] , []
    for col in reader:
        current_date = datetime.strptime(col[2], "%Y-%m-%d")
        try:
            high = (int(col[4])-32)*5/9
            low = (int(col[5])-32)*5/9
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates[-120:], highs[-120:], c='red', alpha=0.5)
ax.plot(dates[-120:], lows[-120:], c='blue', alpha=0.5)
fig1, ax1 = plt.subplots()
ax1.plot(dates[-485:-365], highs[-485:-365], c='red')
ax1.plot(dates[-485:-365], lows[-485:-365], c='blue')
fig1.autofmt_xdate()

# Format plot.
plt.title("Daily high and low temperatures, 2021\nLinkoping Ost.", fontsize=21)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel('Temperature (c)', fontsize=16)
fig.autofmt_xdate() # To formate date in automatic way
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
