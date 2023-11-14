# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 11
# Date: 11/15/2023
#

# comment
from statistics import *

with open("WeatherDataCLL.csv", "r+") as w_data:
    sort_list_data = []
    line_data = w_data.read()
    list_data = line_data.split("\n")
    for i in list_data:
        sort_list_data.append(i.split(","))

    max_temp_list = []
    for d in sort_list_data:
        if len(d[5]) > 4:
            continue
        if d[5] == "":
            continue
        else:
            max_temp_list.append(int(d[5]))
    print(f"10-year maximum temperature: {max(max_temp_list)} F")

    min_temp_list = []
    for d in sort_list_data:
        if len(d[6]) > 4:
            continue
        if d[6] == "":
            continue
        else:
            min_temp_list.append(int(d[6]))
    print(f"10-year minimum temperature: {min(min_temp_list)} F")

    print()
    month_user = str(input("Please enter a month: "))
    year_user = str(input("Please enter a year: "))
    print()
    print(f"For {month_user} {year_user}:")
    month_dict = {
        "January": "1/",
        "February": "2/",
        "March": "3/",
        "April": "4/",
        "May": "5/",
        "June": "6/",
        "July": "7/",
        "August": "8/",
        "September": "9/",
        "October": "10/",
        "November": "11/",
        "December": "12/",
    }
    values_list = []
    for dp in sort_list_data:
        if (
            (month_dict[month_user] == "10/")
            or (month_dict[month_user] == "11/")
            or (month_dict[month_user] == "12/")
        ):
            if month_dict[month_user] in dp[0][:3] and year_user in dp[0][4:]:
                values_list.append(dp)
        else:
            if month_dict[month_user] in dp[0][0:2] and year_user in dp[0][4:]:
                values_list.append(dp)

    avg_temp_list = []
    a = 0
    for d in values_list:
        if len(d[4]) > 6:
            continue
        if d[4] == "":
            avg_temp_list.append(0)
        else:
            avg_temp_list.append(float(d[4]))
    print(f"Mean average daily temperature: {mean(avg_temp_list):.1f} F")

    rel_humidity_list = []
    for d in values_list:
        if len(d[3]) > 6:
            continue
        if d[3] == "":
            continue
        else:
            rel_humidity_list.append(float(d[3]))
    print(f"Mean relative humidity: {mean(rel_humidity_list):.1f} %")

    wind_speed_list = []
    for d in values_list:
        if len(d[1]) > 6:
            continue
        if d[1] == "":
            continue
        else:
            wind_speed_list.append(float(d[1]))
    print(f"Mean daily wind speed: {mean(wind_speed_list):.2f} mph")

    days_total = 0
    days_p = 0
    for d in values_list:
        if len(d[2]) > 6:
            continue
        if d[2] == "":
            days_total += 1
            continue
        if d[2] == "0":
            days_total += 1
            continue
        else:
            days_total += 1
            days_p += 1
    print(f"Percentage of days with precipitation: {((days_p/days_total)*100):.1f} %")
