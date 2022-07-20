import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get date and rain from file
    dates, rains = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        dates.append(current_date)
        rains.append(rain)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rains, linewidth=3)
    fig.autofmt_xdate() 
    ax.set_title("The annual rain fall amount in Stika 2018", fontsize=24)
    ax.set_xlabel('')
    ax.set_ylabel('Rain fall', fontsize=12)

    plt.show()

