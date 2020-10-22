### Iteration Refresher

# number = list(range(1, 11))

## Running in the shell the fol. will dem. that it is an iterable:
# print('__iter__' in dir('number'))

# it = iter('string')
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

## This will not throw and error when it gets to the end
# for char in 'string':
#     print(char)

### Itertools - Cycle
import itertools, sys, time

symbols = itertools.cycle('-\|/')

while True:
    sys.stdout.write('\r' + next(symbols)) # '\r' -- will make sure that the iteritems will be displayed on the same line
    sys.stdout.flush()
    time.sleep(0.3)
