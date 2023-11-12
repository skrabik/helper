import datetime

year = 2023
month, day, hour, min = map(int, input().split())

dt_now = datetime.datetime(year, month, day, hour, min)

dt = datetime.datetime(year, month, day, hour, min)

print(dt_now == dt)
