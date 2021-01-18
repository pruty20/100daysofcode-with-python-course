from datetime import datetime
from datetime import date

# print(datetime.today())

# today = datetime.today()
# print(type(today))

todaydate = date.today()
# print(type(todaydate))
# print(todaydate)
# print(todaydate.month)
# print(todaydate.day)
# print(todaydate.year)

christmas = date(2021, 12, 25)
print(christmas)
print(christmas-todaydate)
print((christmas-todaydate).days)

if christmas != todaydate:
    print("Sorry, there are still " + str((christmas-todaydate).days) + " days until Christmas")
else:
    print("Yay, it's Christmas")