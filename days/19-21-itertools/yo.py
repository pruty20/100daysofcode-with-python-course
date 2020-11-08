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

# ### Itertools - Cycle
# import itertools, sys, time
#
# symbols = itertools.cycle('-\|/')
#
# while True:
#     sys.stdout.write('\r' + next(symbols)) # '\r' -- will make sure that the iteritems will be displayed on the same line
#     sys.stdout.flush()
#     time.sleep(0.3)

# ### Itertools - Product
# from itertools import product
#
# # will return cartezian product (every possible combination)
# for letter in product("razvan", repeat=2):
#     print(letter)

# ### Itertools - Combinations and Permutations
# from itertools import permutations, combinations
#
# friends = 'mike bob julian'.split()
#
# print(list(combinations(friends, 2)))
#
# print(list(permutations(friends, 2)))


# # Exercise for traffic lights -- mine
"""
Day N+1: Create a Traffic Lights script

Yep that's right! For your second day, use itertools to create a script that simulates traffic lights!

The idea is to perhaps... cycle (hint hint!) through the different colours of a set of traffic lights -
red, amber and green - printing the name of the colour every time the cycle occurs.

For bonus points: traffic lights normally cycle between green and red based on traffic levels so you never know exactly
when the change will happen. This is a great chance to throw some randomness into your script.
"""
# import itertools, time
#
# lights = itertools.cycle(['red', 'yellow',  'green'])
# for el in lights:
#     print(el)
#     time.sleep(3)


# # Solution
# from time import sleep
# import itertools, random
#
# colours = 'Red Amber Green'.split()
# rotation = itertools.cycle(colours)
#
# def rg_time():
#     return random.randint(3, 7)
#
# def light_rotation(rotation):
#     for colour in rotation:
#         if colour == 'Amber':
#             print(f"Caution! The light is {colour}")
#             sleep(rg_time())
#         elif colour == 'Red':
#             print(f"STOP! The light is {colour}")
#             sleep(rg_time())
#         else:
#             print(f"GO! The light is {colour}")
#             sleep(3)


if __name__ == '__main__':
    light_rotation(rotation)










