from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

"""
namedtuple -- convenient way to define a class without methods. 
This allows to store dict like objects you can access by attributes.
"""

# ## classic tuple:
# user = ('bob', 'coder')
# print(f'{user[0]} is a {user[1]}')
#
# ## namedtuple: -- first argument is the tuple name and after are the elements
# User = namedtuple('User', 'name role')
# user = User(name='bob', role='coder')
# print(user.name)
# print(user.role)
# print(f'{user.name} is a {user.role}')


"""
defaultdict
"""

## a simple dictionary
users = {'bob': 'coder'}
# print(users['bob'])
# print(users['boby']) ## in order not to get an exception use .get which will return None if there is no key

# print(users.get('bob'))
# print(users.get('boby'))

## a list of tuples
challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]
# print(challenges_done)

# ## converting to a dictionary
# challenges = {}
# for name, challenge in challenges_done:
#     challenges[name].append(challenge) ## will return an error since 'mike' is not already in the dictionary

## defaultdict
challenges = defaultdict(list) #adding the type of data used
for name, challenge in challenges_done:
    challenges[name].append(challenge)
print(challenges)

