"""
Lists are great but for inserts, but if elements need to be added at the start,
on a big sample, they get very slow.
Deques are great for removing and inserting at the both ends of the sequence.
"""
from collections import deque
import random
from timeit import timeit

lst = list(range(10000000))
deq = deque(range(10000000))

def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)




## this will work only using Jupyter Workbook since this is a magic method for it
# %timeit insert_and_delete(lst)
# %timeit insert_and_delete(deq)

# insert_and_delete(lst)
# insert_and_delete(deq)

