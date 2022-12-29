import datetime
birthday = datetime.date(2014,2,21)
now = datetime.date.today()
delta = now - birthday
print(delta.days)

