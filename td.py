import datetime as dt

# Assign Date
valentine_date = dt.datetime(year=2022, month=2, day=14)
print(valentine_date)

# Calculate datetime pass.
day_forward = dt.timedelta(days=30)
target_date = valentine_date + day_forward
print(target_date)

# Calculate distance between two dates.
date1 = dt.datetime(year=2021, month=1, day=1)
date2 = dt.datetime(year=2021, month=5, day=11)
distance = date2 - date1
print(distance)

# Date-Time in String Format Time format
# Link: https://www.w3schools.com/python/gloss_python_date_format_codes.asp
print(valentine_date.strftime("%Y/%B/%d"))



