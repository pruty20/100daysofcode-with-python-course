

### Itertools - Combinations and Permutations
from itertools import permutations, combinations

friends = 'mike bob julian'.split()

print(list(combinations(friends, 2)))

print(list(permutations(friends, 2)))

### Itertools - Product
from itertools import product

# will return cartesian product (every possible combination)
for letter in product("razvan", repeat=3):
    print(letter)