from datetime import datetime
from datetime import date

# print(datetime.today())

# today = datetime.today()
# print(type(today))

# todaydate = date.today()
# # print(type(todaydate))
# # print(todaydate)
# # print(todaydate.month)
# # print(todaydate.day)
# # print(todaydate.year)

# christmas = date(2021, 12, 25)
# print(christmas)
# print(christmas-todaydate)
# print((christmas-todaydate).days)

# if christmas != todaydate:
#     print("Sorry, there are still " + str((christmas-todaydate).days) + " days until Christmas")
# else:
#     print("Yay, it's Christmas")

### Time delta
from datetime import timedelta

t = timedelta(days=4, hours=10)
# print(type(t))
print(t.days)
print(t.seconds) ## its only able to show seconds for one full day e.g: hours=23, minultes=59, seconds=59
print(t.seconds / 60 / 60) ## will convert to hours OR t.seconds / 3600  /// t.hours --> will fail

eta = timedelta(hours=6)
today = datetime.today()
print(today)
print(eta)
print(today + eta)
print(str(today + eta))














