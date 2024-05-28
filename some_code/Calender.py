import calendar


import time

currenttime= time.localtime(time.time())
print("Current time is", currenttime)


def print_calender(year, month):
    cal = calendar.month(year, month)
    return cal

year =  2024
month = 12
print(print_calender(year, month))