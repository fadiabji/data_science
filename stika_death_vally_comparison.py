import csv
import matplotlib.pyplot as plt
from datetime import datetime


def extract_dates_temps(filename='data/sitka_weather_2018_simple.csv'):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column_header in enumerate(header_row):
            print(index, column_header)
        dates, temp = [], []
        
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                tempreture = (int(row[5]) + int(row[6]))/2
                dates.append(current_date)
                temp.append(tempreture)
            except ValueError:
                print(f"Missing data at {current_date}.")
        return dates, temp

stika_dates, stika_temps = extract_dates_temps('data/sitka_weather_2018_simple.csv')
death_v_dates, death_v_temps = extract_dates_temps('data/death_valley_2018_simple.csv')


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot()
plt.plot(stika_dates, stika_temps, label="Death Valley", c='yellow')
plt.plot(stika_dates, death_v_temps, label="Stika", c="blue")
plt.legend()

fig.autofmt_xdate() 
ax.set_title("The annual rain fall amount \nin Stika and Death_valley 2018", fontsize=24)
ax.set_xlabel('')
ax.set_ylabel('Rain fall', fontsize=12)

plt.show()
