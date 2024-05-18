import datetime
import calendar

month, date, year = map(int, input().split())
input_date = datetime.date(year, month, date)
print(calendar.day_name[input_date.weekday()].upper())
