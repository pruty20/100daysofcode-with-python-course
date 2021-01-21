"""
Manipulating lists
"""

# numlist = [1, 2, 3, 4, 5]
#
# print(numlist)
#
# numlist.reverse()
# print(numlist)
#
# numlist.sort()
# print(numlist)
#
# for num in numlist:
#     print(str(num))
#
# mystring = 'julian'
# mystring_list = list(mystring)
# print(mystring_list)
#
# print(mystring_list[4])
# print(mystring_list.pop())
#
# print(mystring_list)
# mystring_list.insert(5, 'n')
#
# print(mystring_list)
# mystring_list[0] = 'b'
# print(mystring_list)
#
# del mystring_list[0]
# print(mystring_list)
#
# mystring_list.insert(0, 'm')
# print(mystring_list)
#
# print(mystring_list.pop(0))
# print(mystring_list)
#
# mystring_list.append('s')
# print(mystring_list)
#
# del mystring_list[0]
# print(mystring_list)

"""
Immutability(cannot be changed) and Tuples -- cannot be edited since are immutable
"""
# mystring = 'julian'
#
# l = list(mystring)
# t = tuple(mystring)
#
# print(l)
# print(t)
#
# l[0] = 't'
# print(l)
#
# ## t[0] = 't' --> will throw an exception since is immutable
#
# # but we can view or return elements from the tuple (t)
# for letter in t:
#     print(letter)

"""
Dictionaries
-- no guarantee that the data will remain in order (they are unordered)
"""
# pybites = {'julian': 30, 'bob': 33, 'mike': 33}
# print(pybites)
#
# people = {}
# people['julian'] = 30
# people['bob'] = 103

# print(people)
#
# print(people.keys())
# print(people.values())
# print(people.items())
#
# for keys in people.keys():
#     print(keys)
#
# for values in people.values():
#     print(values)

# for keys, values in people.items():
#     # print('%s is %d years of age' % (keys, values))
#     print(f'{keys} is {values} years of age')

