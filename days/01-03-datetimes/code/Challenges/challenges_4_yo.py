"""
You've got the basics down so now create something for yourself!

A fun project would be to create yourself a Pomodoro Timer that incorporates datetime
rather than just the time module. Have it display timestamps.

This could also be applied to a stopwatch app.
Use time of course but also throw in the timestamps and even some basic calculations
on the difference between the start and end timestamps.

We encourage you to pull request your work via PyBites Code Challenge #52
(https://codechalleng.es/challenges/)
 Have fun!
"""
from datetime import datetime, timedelta
import time

counter = 0
now = datetime.now()
noww = datetime.now()




while now + timedelta(seconds=5) > datetime.now():
    print(datetime.now())












# while counter < 20:
#     # start = start + timedelta(seconds=1)
#     counter += 1


#
# print(datetime.now())
# print(datetime.now() + timedelta(seconds=100))

# t_delta = timedelta(days=2, hours=2, seconds=3)
# print(t_delta)