
"""
1.
In this bite we will look at this small server log finding the first
and last system shutdown events:

INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
...
INFO 2014-07-03T23:31:22 supybot Shutdown initiated.

You need to calculate the time between these two events.
First extract the timestamps from the log entries
and convert them to datetime objects.
Then use datetime.timedelta to calculate the time difference between them.

You can assume the logs are sorted in ascending order.
Check out the docstrings and the TESTS for more info.
"""
from email import utils

import re

def convert_to_datetime(line="INFO 2014-07-03T23:27:51 supybot Shutdown complete"):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    # regex = re.compile(r'\b\d{4}[-/]\d{2}[-/]\d{2}\s\d{2}:\d{2}:\d{2}\s[-+]\d{4}\b')
    # n = regex.findall(line)
    # m = re.search("(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})", line)
    # print(n)


convert_to_datetime()

import re
m = re.findall("(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})", "INFO 2014-07-03T23:27:51 supybot Shutdown complete.")
char_to_replace = ["-", "T", ":"]
n = m[0]
for char in char_to_replace:
    n = n.replace(char, ", ")

print(n)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    pass
