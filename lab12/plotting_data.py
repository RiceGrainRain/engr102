# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 12
# Date: 11/20/2023
#

# comment

import matplotlib.pyplot as plt
from csv import reader
import numpy as np
from datetime import datetime

file_name = "WeatherDataCll.csv"

day_list, temperature_list, wind_index_list, wind_speed_list = [], [], [], []

with open(file_name, "r") as file:
    csv_reader = reader(file, delimiter=",")
    next(csv_reader)
    for i, row in enumerate(csv_reader, start=1):
        if row[5] != "":
            day_list.append(i)
            temperature_list.append(float(row[5]))

        if row[1] != "":
            wind_index_list.append(i)
            wind_speed_list.append(float(row[1]))

days, max_temp, wind_indices, avg_wind_speed = (
    np.array(day_list),
    np.array(temperature_list),
    np.array(wind_index_list),
    np.array(wind_speed_list),
)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(days, max_temp, linestyle="-", color="red", label="Max temp")
ax2.plot(
    [0], [0], linestyle="-", marker="None", markersize=0, color="red", label="Max Temp"
)
ax2.plot(wind_indices, avg_wind_speed, linestyle="-", color="blue", label="Avg Wind")

ax2.legend(loc="lower left")
plt.title("Max Temperature and Avg Wind Speed Over Time")
ax1.set_xlabel("Date")
ax1.set_ylabel("Max Temperature in F°")
ax2.set_ylabel("Avg Wind Speed in mph")

plt.show()

with open(file_name, "r") as file:
    humidity_list = []
    precipitation_list = []
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        if row[2] == "" or row[3] == "":
            continue
        else:
            row[3].rstrip(",")
            humidity_list.append(int(row[3]))
            precipitation_list.append(float(row[2]))
    humidity_arr = np.array(humidity_list)
    precipitation_arr = np.array(precipitation_list)

plt.scatter(humidity_arr, precipitation_arr, marker=".", color="black")
plt.title("Precipitation vs. Avg Relative Humidity")
plt.xlabel("Avg Relative Humidity (%)")
plt.ylabel("Precipitation (in)")
plt.show()

with open(file_name, "r") as file:
    csv_reader = reader(file, delimiter=",")
    next(csv_reader)
    wind_speeds = [
        float(row[1])
        for row in csv_reader
        if row[1] and row[1] != "Average Daily Wind Speed (mph)"
    ]
wind_speed_arr = np.array(wind_speeds)

plt.hist(wind_speed_arr, bins=29, color="green", edgecolor="black")
plt.title("Histogram of Avg Wind Speeds")
plt.ylabel("Number of Days")
plt.xlabel("Avg Wind Speed in mph")
plt.show()

# Last section
with open(file_name, "r") as file:
    csv_reader = reader(file)
    next(csv_reader)

    months = {i: [] for i in range(1, 13)}
    months_max = {i: [] for i in range(1, 13)}
    months_min = {i: [] for i in range(1, 13)}

    for line in csv_reader:
        try:
            date = datetime.strptime(line[0], "%m/%d/%Y")
            month = date.month
            month_data = [int(val) if val else np.nan for val in line[-3:]]
            months[month].append(month_data[0])
            months_max[month].append(month_data[1])
            months_min[month].append(month_data[2])
        except (ValueError, IndexError):
            continue

month_avg = [np.nanmean(months[i]) for i in range(1, 13)]
month_max_temp = [np.nanmax(months_max[i]) for i in range(1, 13)]
month_min_temp = [np.nanmin(months_min[i]) for i in range(1, 13)]

x = np.arange(1, 13)
x_labels = [datetime.strptime(str(i), "%m").strftime("%b") for i in range(1, 13)]

plt.bar(x, month_avg, color="y")
plt.title("Temp by Month")
plt.xticks(x, x_labels)
plt.xlabel("Month")
plt.ylabel("Avg Temperature in F°")
plt.plot(x, month_max_temp, color="red", label="High T")
plt.plot(x, month_min_temp, color="blue", label="Low T")
plt.legend(loc="upper right")
plt.show()
