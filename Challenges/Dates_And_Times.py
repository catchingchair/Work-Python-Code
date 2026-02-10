# Count the number of instances of a particular weekday in a given month/year
# you are given a month and a year along with a day of the week (monday-sunday)
# your task: return the number of instances of that day of the week in thegiven month. 
import calendar

def count_days(year, month, whichday):
    count = 0
    weeks = calendar.monthcalendar(year, month)
    for week in weeks:
        if week[whichday] != 0:
            count += 1
    return count

    