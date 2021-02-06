"""
Iteration refresher
"""

number = list(range(1, 11))

# one way to demonstrate that the number list is iterable
print('__iter__' in dir(number))

for i in number:
    print(i)

# one other way to check if an element is iterable, is to use next()
#  when it finishes to iterate it will throw an exception stopIteration
it = iter('string')
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) ## This will throw StopIteration since the iteration is done
#  when running a for loop instead it will handle the exception




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
#     sys.stdout.write('\r' + next(symbols)) # '\r' -- will make sure that the iteritems will be displayed on the same line/row/position
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

# import itertools
#
# def friends_teams(friends, team_size=2, order_does_matter=False):
#     if order_does_matter:
#         func = itertools.permutations
#     else:
#         func = itertools.combinations
#     return func(friends, team_size)

# ex = friends_teams(['Bob', 'Dante', 'Julian'], team_size=2, order_does_matter=True)

# for el in ex:
#     print(el)



"""
https://codechalleng.es/bites/65/
Get all valid dictionary words for a draw of letters 

This Bite focusses on the use of itertools. 
To that extend you complete get_possible_dict_words and _get_permutations_draw to get all valid dictionary words 
for a random draw of 7 letters.

This is fed into the tests that calculate the word with maximum value 
(work previously done for Bite 3) https://codechalleng.es/bites/3/ and there you go: you have a Scrabble cheat tool 
(Scrabble fans, pay attention or maybe skip this Bite!).

For example a draw of letters G, A, R, Y, T, E, V would give highest valued word GARVEY (13 points).

This Bite is adapted from PyBites Code Challenge 02: Word Values Part II - A Simple Game. 
https://codechalleng.es/challenges/2/ 
Check it out if you want to code up the complete game including the user interaction part.
"""


if __name__ == '__main__':
    pass







