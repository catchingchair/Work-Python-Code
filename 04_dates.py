# Date Objects

from datetime import date
from datetime import datetime

# Get today's date from the simple today() method from the date class
today = date.today()
print(f"Today's date is {today}")

# print out the date's individual components
print(f"Date Components: {today.day}, {today.month}, {today.year}")

# retrieve today's weekday (0 = Monday, 6 = Sunday)
print(f"Today's Weekday #: {today.weekday()}")

## DATETIME OBJECTS
# Get today's date from the datetime class
today2 = datetime.today()
print(f"The current date and time is {today2}")

# Get the current time
t = datetime.time(datetime.now())
print(f"The current time is {t}")