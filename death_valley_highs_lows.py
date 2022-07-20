import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
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
            high = int(col[4])
            low = int(col[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

# Format plot.
plt.title("Daily high temperatures, 2018\nDeath Valley, CA", fontsize=24)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
fig.autofmt_xdate() # To formate date in automatic way
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

