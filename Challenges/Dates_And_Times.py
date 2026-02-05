# Count the number of instances of a particular weekday in a given month/year
# you are given a month and a year along with a day of the week (monday-sunday)
# your task: return the number of instances of that day of the week in thegiven month. 
import calendar

def count_days(year, month, whichday):
    daycount = 0
    weekslist = calendar.monthcalendar(year, month)
    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

    