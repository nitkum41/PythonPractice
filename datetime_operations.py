import time
from datetime_operations import datetime
from datetime_operations import timedelta

print(time.timezone)


print(datetime.now().date()) ##todays date

today_date=datetime.now().date()


print(today_date-timedelta(days=1))  # a day before
