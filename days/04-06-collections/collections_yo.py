from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from timeit import timeit
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

# ## defaultdict
# challenges = defaultdict(list) #adding the type of data used
# for name, challenge in challenges_done:
#     challenges[name].append(challenge)
# print(challenges)

"""
counter
"""
# words = """"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""".split()
#
# # without using collections
# common_words = {}
#
# for word in words:
#     if word not in common_words:
#         common_words[word] = 0
#     common_words[word] += 1
#
# for k, v in sorted(common_words.items(),
#                    key=lambda x: x[1],
#                    reverse=True)[:6]:
#     print(k,v)
#
# #using counter from collections
# Counter(words).most_common(5)

"""
deque --> you can also check OrderedDict (in 3.6 dicts are ordered by default) and ChainMap in docs 
"""
lst = list(range(10000000))
deq = deque(range(1000000))

def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

# %timeit insert_and_delete(lst) -- this can be run only from the py console
# %timeit insert_and_delete(deq)