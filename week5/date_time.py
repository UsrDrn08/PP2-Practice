"""from datetime import timedelta, datetime

current_date = datetime.now()
result = current_date - timedelta(days = 5)
print(result.strftime("%Y-%m-%d"))
"""
"""
from datetime import datetime, timedelta
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(today, yesterday, tomorrow)
"""
"""
from datetime import datetime
dt_with = datetime.now()
dt_without = dt_with.replace(microsecond=0)
print(dt_without)
""" 
"""from datetime import datetime
import time 
date1 = datetime.now()
time.sleep(2)
date2 = datetime.now()
dif = date1 - date2
sec = dif.total_seconds()
print(sec)
"""