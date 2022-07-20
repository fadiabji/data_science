import csv
import matplotlib.pyplot as plt
from datetime import datetime


def extract_dates_highs_lows_stika(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)
        dates, highs, lows = [], [], []
        
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[5])
                low = int(row[6])
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
            except ValueError:
                print(f"Missing data at {current_date}.")
        return dates, highs, lows

def extract_dates_highs_lows_san_f(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)
        dates, highs, lows = [], [], []
        
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[4])
                low = int(row[5])
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
            except ValueError:
                print(f"Missing data at {current_date}.")
        return dates, highs, lows


stika_dates, stika_highs, stika_lows = extract_dates_highs_lows_stika('data/sitka_weather_2018_simple.csv')
san_f_dates, san_f_highs, san_f_lows = extract_dates_highs_lows_san_f('data/san_francisco_2018.csv')


plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.plot(stika_dates, stika_highs, label="Stika highs", c='yellow')
plt.plot(stika_dates, stika_lows, label="Stika lows", c="blue")
plt.legend()

fig.autofmt_xdate() 

fig1, ax1 = plt.subplots()
ax1.plot(san_f_dates, san_f_highs, label="san highs", c='red')
ax1.plot(san_f_dates, san_f_lows, label="san lows", c="blue")
plt.legend()
fig1.autofmt_xdate()
fig.autofmt_xdate() 

ax.set_title("", fontsize=24)
ax.set_xlabel('')
ax.set_ylabel('', fontsize=12)

plt.show()
