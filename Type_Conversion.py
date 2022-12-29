import datetime
birth_year = input("Birth year: ")
today = datetime.date.today()
year = today.year
print(type(birth_year))
age = year - int(birth_year)
print(type(age))
print(f'You are {age} years old.')