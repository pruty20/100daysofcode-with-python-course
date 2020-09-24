import itertools
import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

# # Can you write a simple list comprehension to convert these names to title case (brad pitt -> Brad Pitt).
title_case_comp = [name.title() for name in NAMES]

# # Or reverse the first and last name?
reversed_comp = [name.split(' ')[1].title() + " " + name.split(' ')[0].title() for name in NAMES] # this was mine

# # Solution from course:
def reverse_first_last_names(name):
    first, last = name.split()
    return f"{last} {first}"

reversed_comp_sol = [reverse_first_last_names(name) for name in NAMES]

"""
Then use this same list and make a little generator, for example to randomly return a pair of names, 
try to make this work:

pairs = gen_pairs()
for _ in range(10):
    next(pairs)
Should print (values might change as random):

Arnold teams up with Brad
Alec teams up with Julian
"""
# def gen_pairs():

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def gen_pairs():
    first_names = [name.split()[0] for name in NAMES]
    while True:
        first, second = None, None
        while first == second:
            first, second = random.sample(first_names, 2)
            yield f"{first} teams up with {second}"

pairs = gen_pairs()
# for _ in range(20):
#     print(next(pairs))

# # Another way to get a slice of a generator is using itertools.islice
first_ten = itertools.islice(pairs, 3)
print(list(first_ten))










