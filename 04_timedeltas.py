# timedeltas

from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it

print(timedelta(days=365,hours=5,minutes=1))

#print todays date
now = datetime.now()

print(f"Today is {now}")

# print today's date one year from now
print(f"In one year it will be: {now+timedelta(days=365)}")

# create a timedelta that uses more than one argument
print(f"In two weeks and 3 days it will be: {now + timedelta(weeks=3,days=3)}")

#calculate the date 1 week agon, formatted as a string
print(f"One week ago it was: {now-timedelta(weeks=1)}")

t = datetime.now() - timedelta(weeks=2)
s = t.strftime("%A %B %d, %Y")
print(f"Two weeks ago it was: {s}")

# How many days until April Fools' Day?
today = date.today()
afd = date(today.year,month=4,day=1)
if afd < today:
    print(f"April fools' day already went by {(today-afd).days} days ago")
    afd = afd.replace(year=today.year+1)

time_to_afd = afd-today
print(f"It's just {time_to_afd.days} days until April Fools' Day")
