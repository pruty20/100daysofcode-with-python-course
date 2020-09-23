from collections import namedtuple

user = ('bob', 'coder')
print(f'{user[0]} is a {user[1]}')

User = namedtuple('User', 'name role')

user = User(name='bob', role='coder')
print(f'{user.name} is a {user.role}')
