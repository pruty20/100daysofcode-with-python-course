
# values printed out will not be ordered
pybites = {'julian': 30,
           'bob': 33,
           'mike': 33}

# empty dict
people = {}

people['julian'] = 30
people['raz'] = 34

print(people, '\n')
print(pybites.keys(), '\n')
print(pybites.values(), '\n')

# will print both the key and value pairs
print(pybites.items(), '\n')

for keys in pybites.keys():
    print(keys)

print('\n')

for values in pybites.values():
    print(values)

print('\n')

for keys, values in pybites.items():
    print('%s is %d years of age' %(keys, values))

print('\n')

for keys, values in pybites.items():
    print(f'{keys}: {values}')

print('\n')