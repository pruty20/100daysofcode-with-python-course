"""
Great at building a nested data structure
-- The value gets initialised before appending to it.
"""
from collections import defaultdict

users = {'bob': 'coder'}
print(users['bob'])
# print(users['julian']) ##will crash since the key is not present

print(f'Checking users.get("bob") has the result: {users.get("bob")}')
print(f'Checking [users.get("julian") is None] has the result: {users.get("julian") is None}')

challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]
print(f'Printing typeof(challenges_done: {type(challenges_done)})')
print(f'\nPrinting challenges_done after initialization:\n {challenges_done}')

# challenges = {}
# for name, challenge in challenges_done:
#     challenges[name].append(challenge)    ##--> KeyError: 'mike'

challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)
print(f'\nPrinting challenges as defaultDict: {challenges}')
