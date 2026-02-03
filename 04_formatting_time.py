from datetime import datetime

# times and dates can be formatted using a set of predefined string control codes
now = datetime.now()

#### DATE FORMATTING ####
# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of the month
print(now.strftime("The current year is: %Y"))
print(now.strftime("%A,%d %B, %y"))

# %c - locale's date and time, %x - locale's date, %X - locale's time
print(now.strftime("Local date and time: %c"))
print(now.strftime("Local date: %x"))
print(now.strftime("Local time: %X"))

#### TIME FORMATTING ####
# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("Current time: %I:%M:%S %p"))
print(now.strftime("Current time: %H:%M"))