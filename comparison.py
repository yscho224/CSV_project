import csv
from datetime import datetime
from matplotlib import pyplot as plt

# death valley file
open_file1 = open("death_valley_2018_simple.csv", "r")

csv_file1 = csv.reader(open_file1, delimiter = ",")

header_row1 = next(csv_file1)

# sitka weather file

open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file2 = csv.reader(open_file2, delimiter = ",")

header_row2 = next(csv_file2)


# sitka
name_index2 = header_row2.index('NAME')
date_index2 = header_row2.index('DATE')
high_index2 = header_row2.index('TMAX')
low_index2 = header_row2.index('TMIN')
highs2 = []
dates2 = []
lows2 = []
'''
x = datetime.strptime('2018-01-01', '%Y-%m-%d')
print(x)
'''
for row in csv_file2:
    the_date = datetime.strptime(row[date_index2], '%Y-%m-%d')
    try:
        high = int(row[high_index2])
        low = int(row[low_index2])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(the_date)

# death valley
name_index1 = header_row1.index('NAME')
date_index1 = header_row1.index('DATE')
high_index1 = header_row1.index('TMAX')
low_index1 = header_row1.index('TMIN')
highs1 = []
dates1 = []
lows1 = []  

for row in csv_file1:
    the_date = datetime.strptime(row[date_index1], '%Y-%m-%d')
    try:
        high = int(row[high_index1])
        low = int(row[low_index1])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs1.append(high)
        lows1.append(low)
        dates1.append(the_date)

fig,ax = plt.subplots(2,1)

fig.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US", fontsize = '14')


ax[0].plot(dates2, highs2, c= "red", alpha = 0.5)
ax[0].plot(dates2, lows2, c= "blue", alpha = 0.5)
ax[0].set_title("SITKA AIRPORT", fontsize = 16)
ax[0].set_xlabel("")
ax[0].fill_between(dates2, highs2, lows2, facecolor = 'blue', alpha = 0.1)
ax[0].set_ylabel("Temperature (F)", fontsize = 16)


ax[1].plot(dates1, highs1, c= "red", alpha = 0.5)
ax[1].plot(dates1, lows1, c= "blue", alpha = 0.5)
ax[1].set_title("DEATH VALLEY, CA US", fontsize = 16)
ax[1].set_xlabel("")
ax[1].fill_between(dates1, highs1, lows1, facecolor = 'blue', alpha = 0.1)
ax[1].set_ylabel("Temperature (F)", fontsize = 16)

plt.tick_params(axis = "both", labelsize = 16)

fig.autofmt_xdate()

plt.show()
