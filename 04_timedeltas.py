# timedeltas

from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timiedelta and print it

print(timedelta(days=365,hours=5,minutes=1))

#print todays date
now = datetime.now()

print(f"Today is {now}")

# print today's date one year from now
print(f"In one year it will be: {now+timedelta(days=365)}")
