from datetime import datetime
import csv
from matplotlib import pyplot as plt


filename = 'sitka_weather_07-2014.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    dates, precipitations = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            precipitation = row[19]
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            precipitations.append(precipitation)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, precipitations, c='red')
plt.title("Daily precipitation - 2014\nSitka, AL", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Precipitation', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
# Precipitation is 19!
