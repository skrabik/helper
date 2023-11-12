import datetime

def get_date(string):
    year = datetime.datetime.now().year
    month, day, hour, min = map(int, string.split())
    rez = datetime.datetime(year, month, day, hour, min, 0, 0)
    return rez

def get_date_in_advance(string):
    year = datetime.datetime.now().year
    month, day, hour, min = map(int, string.split())
    rez = datetime.datetime(year, month, day, hour, min, 0, 0)

    rez -= datetime.timedelta(minutes=30)

    return rez


