import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Max/min temperature and date reading.
filename_1 = 'death_valley_2014.csv'
filename_2 = 'sitka_weather_2014.csv'
with open(filename_1) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    dates_1, highs_1, lows_1 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = (int(row[1]) - 32) * 5/9
            low = (int(row[3]) - 32) * 5/9
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs_1.append(high)
            dates_1.append(current_date)
            lows_1.append(low)
    # print(highs)

with open(filename_2) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    dates_2, highs_2, lows_2 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = (int(row[1]) - 32) * 5 / 9
            low = (int(row[3]) - 32) * 5 / 9
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs_2.append(high)
            dates_2.append(current_date)
            lows_2.append(low)

# Moving data on diagram.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_1, highs_1, c='red', alpha=0.5)
plt.plot(dates_1, lows_1, c='blue', alpha=0.5)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.1)
plt.plot(dates_2, highs_2, c='green', alpha=0.5)
plt.plot(dates_2, lows_2, c='yellow', alpha=0.5)
plt.fill_between(dates_2, highs_2, lows_2, facecolor='blue', alpha=0.1)

# Formation of diagram.
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA & Sitka, AL", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (С)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
