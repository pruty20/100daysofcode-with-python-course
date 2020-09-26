
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
from datetime import datetime
from email import utils

import re

def convert_to_datetime(line="INFO 2016-09-03T02:11:22 supybot Shutdown complete."):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    import re
    m = re.findall("(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})", line)
    char_to_replace = ["-", "T", ":"]
    n = m[0]
    for char in char_to_replace:
        n = n.replace(char, ", ")
        list_str = n.split(",")

    list_num = []
    for number in list_str:
        list_num.append(int(number))

    date_yo = datetime(list_num[0], list_num[1], list_num[2],
                       list_num[3], list_num[4], list_num[5])
    return date_yo


# convert_to_datetime()

loglines = """ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file, resetting to empty.
ERROR 2014-07-03T23:24:31 supybot Exact error: IOError: [Errno 2] No such file or directory: 'conf/users.conf'
ERROR 2014-07-03T23:24:31 supybot Invalid channel database, resetting to empty."""


def time_between_shutdowns(loglines=loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    print(loglines)


time_between_shutdowns()



