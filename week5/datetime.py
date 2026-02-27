import datetime

now = datetime.datetime.now()
specific_date = datetime.datetime(2023, 5, 17, 12, 30)
print(specific_date)

#difference of time
d1 = datetime.datetime(2026, 1, 1)
d2 = datetime.datetime(2026, 2, 1)
diff = d2 - d1
print(diff.days) # 31

#work with different of hours
import zoneinfo 
utc_now = datetime.datetime.now(datetime.timezone.utc)
print(utc_now)