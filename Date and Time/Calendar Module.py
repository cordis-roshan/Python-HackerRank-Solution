from datetime import datetime
month, day, year = map(int, input().split())
date_obj = datetime(year, month, day)
day_of_week = date_obj.strftime('%A').upper()
print(day_of_week)