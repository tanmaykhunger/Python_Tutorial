import datetime
def calculate_days (year,month,day):
    days1 = datetime.date(year, month, day)
    now = datetime.date.today()
    delta = now - days1
    return(delta.days)


calculate_days()