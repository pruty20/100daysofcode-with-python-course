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

time_interval = timedelta(seconds=5)

time_now = datetime.now()
time_end = time_now + time_interval

print(f"Start: {time_now}")
print(f"Stop: {time_end}")

stop = False
while stop == False:
    time_now = datetime.now()
    if time_now >= time_end:
        stop = True
        print(f"Time is up, time is: {datetime.now()}")