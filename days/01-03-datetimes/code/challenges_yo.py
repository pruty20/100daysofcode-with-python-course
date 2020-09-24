
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


def convert_to_datetime(line="INFO 2014-07-03T23:27:51 supybot Shutdown complete"):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    new_line = line.replace("INFO ", "")
    new_line2 = new_line.replace(" supybot Shutdown complete", "")
    new_line3 = new_line2.replace("-", ", ")
    new_line4 = new_line3.replace("T", ", ")
    new_line5 = new_line4.replace(":", ", ")
    new_line6 = new_line5.replace("2014, 07, 03, 23, 27, 51", "datetime(2014, 07, 03, 23, 27, 51)")
    print(new_line6)



convert_to_datetime()


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    pass
