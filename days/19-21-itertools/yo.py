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
# # will return cartesian product (every possible combination)
# for letter in product("razvan", repeat=3):
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
# if __name__ == '__main__':
#     light_rotation(rotation)

"""
CHALLENGES:
https://codechalleng.es/bites/64/
Bite 64. Fix a truncating zip function

Bert is in charge of organizing an event and got the attendees names, locations and confirmations 
in 3 lists. Assuming he got all data and being Pythonic he used zip to stitch them together 
(see template code) but then he sees the output:
('Tim', 'DE', False)
('Bob', 'ES', True)
('Julian', 'AUS', True)
('Carmen', 'NL', False)
('Sofia', 'BR', True)

What?! Mike, Kim, and Andre are missing! You heard somebody mention itertools the other day for 
its power to work with iterators. Maybe it has a convenient way to solve this problem? 
Check out the module and patch the get_attendees function for Bert so it returns all names again. 
For missing data use dashes (-). After the fix Bert should see this output:
('Tim', 'DE', False)
('Bob', 'ES', True)
('Julian', 'AUS', True)
('Carmen', 'NL', False)
('Sofia', 'BR', True)
('Mike', 'US', '-')
('Kim', '-', '-')
('Andre', '-', '-')
"""
# from itertools import zip_longest
#
# names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
# locations = 'DE ES AUS NL BR US'.split()
# confirmed = [False, True, True, False, True]
#
#
# def get_attendees():
#     for participant in zip_longest(names, locations, confirmed, fillvalue='-'):
#         print(participant)
#
#
# if __name__ == '__main__':
#     get_attendees()


"""
https://codechalleng.es/bites/17/
Write a function called friends_teams that takes a list of friends, 
a team_size (type int, default=2) and order_does_matter (type bool, default False).

Return all possible teams. Hint: if order matters (order_does_matter=True), 
the number of teams would be greater.
"""

# TESTS:
# import pytest
#
# from friends import friends_teams
#
# friends = 'Bob Dante Julian Martin'.split()
#
#
# @pytest.mark.parametrize('test_input,expected', [
#     (('Bob', 'Dante'), True),
#     (('Bob', 'Julian'), True),
#     (('Bob', 'Martin'), True),
#     (('Dante', 'Julian'), True),
#     (('Dante', 'Martin'), True),
#     (('Julian', 'Martin'), True),
#     # order does not matter
#     (('Dante', 'Bob'), False),
#     (('Julian', 'Bob'), False),
#     (('Martin', 'Bob'), False),
#     (('Julian', 'Dante'), False),
#     (('Martin', 'Dante'), False),
#     (('Martin', 'Julian'), False),
#     # not with self
#     (('Julian', 'Julian'), False),
# ])
# def test_team_of_two_order_does_not_matter(test_input, expected):
#     """First test lists all combos"""
#     combos = list(friends_teams(friends, team_size=2, order_does_matter=False))
#     assert len(combos) == 6
#     if expected:
#         assert test_input in combos
#     else:
#         assert test_input not in combos
#
#
# @pytest.mark.parametrize('test_input,expected', [
#     (('Bob', 'Dante'), True),
#     (('Dante', 'Julian'), True),
#     (('Dante', 'Martin'), True),
#     # order does matter
#     (('Dante', 'Bob'), True),
#     (('Julian', 'Dante'), True),
#     (('Martin', 'Dante'), True),
# ])
# def test_team_of_two_order_does_matter(test_input, expected):
#     """From here on just test a subset of combos"""
#     combos = list(friends_teams(friends, team_size=2, order_does_matter=True))
#     assert len(combos) == 12
#     assert test_input in combos
#
#
# @pytest.mark.parametrize('test_input,expected', [
#     (('Bob', 'Dante', 'Julian'), True),
#     (('Bob', 'Dante', 'Martin'), True),
#     (('Bob', 'Julian', 'Martin'), True),
#     (('Dante', 'Julian', 'Martin'), True),
#     # order does not matter
#     (('Dante', 'Bob', 'Martin'), False),
#     (('Julian', 'Martin', 'Dante'), False),
#     # no one goes twice
#     (('Dante', 'Dante', 'Martin'), False),
# ])
# def test_team_of_three_order_does_not_matter(test_input, expected):
#     combos = list(friends_teams(friends, team_size=3, order_does_matter=False))
#     assert len(combos) == 4
#     if expected:
#         assert test_input in combos
#     else:
#         assert test_input not in combos
#
#
# @pytest.mark.parametrize('test_input,expected', [
#     (('Bob', 'Dante', 'Julian'), True),
#     (('Bob', 'Dante', 'Martin'), True),
#     (('Bob', 'Julian', 'Martin'), True),
#     (('Dante', 'Julian', 'Martin'), True),
#     # order does matter
#     (('Dante', 'Bob', 'Martin'), True),
#     (('Julian', 'Martin', 'Dante'), True),
# ])
# def test_team_of_three_order_does_matter(test_input, expected):
#     combos = list(friends_teams(friends, team_size=3, order_does_matter=True))
#     assert len(combos) == 24
#     assert test_input in combos



if __name__ == '__main__':
    pass







