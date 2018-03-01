from datetime import datetime
from pytz import timezone

def time_diff(timestamp1, timestamp2):
    # datetime-datetime = datetime.timedelta
    diff = abs(timestamp1-timestamp2) # abs difference
    return round(diff.total_seconds()) # '.seconds' are NOT to be used

# ---

tz1 = timezone('Europe/Amsterdam') # +1
tz2 = timezone('Europe/Tallinn') # +2
dt1 = tz1.localize(datetime(2018, 3, 1, 21, 43, 0, 0))
dt2 = tz2.localize(datetime(2018, 3, 1, 22, 43, 0, 0))

assert time_diff(dt1, dt2) == 0

dt1 = tz1.localize(datetime(2018, 3, 1, 22, 43, 0, 0))
dt2 = tz2.localize(datetime(2018, 3, 1, 22, 43, 0, 0))

assert time_diff(dt1, dt2) == 3600
