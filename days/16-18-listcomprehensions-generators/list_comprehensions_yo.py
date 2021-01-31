from collections import Counter
import calendar
import itertools
import random
import re
import string
import requests

names = 'pybites mike bob julian tim sara guido'.split()

# for name in names:
#     print(name.title())

first_half_alphabet = list(string.ascii_lowercase)[:13]
# print(first_half_alphabet)

new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())

# print(new_names)

"""Start list comprehensions"""
name_list = [name.title() for name in names if name[0] in first_half_alphabet]
# print(f"Printing name list: \n {name_list}")

# new exercise
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
resp = requests.get("http://projects.bobbelderbos.com/pcc/harry.txt", headers=headers)
words = resp.text.lower().split()
cnt = Counter(words)
# print(cnt.most_common(5))
# print('-' in words)

# cleaning up any non-alphabetical characters
#  regex: \W matches any non-alphanumeric character; which is
#   equivalent to the set [^a-zA-Z0-9_]
words = [re.sub(r'\W+', r'', word) for word in words]
# print('-' in words)

# getting another filtering to remove "the" words by using
#  a list of stop words used to filter them out
resp = requests.get("http://projects.bobbelderbos.com/pcc/stopwords.txt", headers=headers)
stopwords = resp.text.lower().split()
words = [word for word in words if word.strip() and word not in stopwords]
cnt = Counter(words)
# print(cnt.most_common(5))

"""
Generators
"""
def num_gen():
    for i in range(5):
        yield i

gen = num_gen()
# print(next(gen))

# for i in gen:
    # print(i)

# this will throw an exception since the above generator
#  has already been consumed if we create the generator
#   again and use a for loop to consume it, the for loop
#    will catch that exception and not throw it
# print(next(gen))

gen = num_gen()
# for i in gen:
#     print(i)

options = 'red yellow blue white green purple'.split()

# without using generators:
def create_select_options(options=options):
    select_list = []

    for option in options:
        select_list.append(f'<option value={option}>{option.title()}</option>')

    return select_list

from pprint import pprint as pp
# pp(create_select_options())

# using the generator
def create_select_options_gen(options=options):
    for option in options:
        yield f'<option value={option}>{option.title()}</option>'

# convert the generator to a list
generator_list = list(create_select_options_gen())
pp(generator_list)



# names = "pybites mike bob julian tim sara guido".split()
#
# # for name in names:
# #     print(name.title())
#
# first_half_alphabet = list(string.ascii_lowercase)[:13]
# # print(first_half_alphabet)
#
# new_names = []
# for name in names:
#     if name[0] in first_half_alphabet:
#         new_names.append(name.title())
# # print(new_names)
#
# ## List Comprehensions
# list_comp = [name.title() for name in names if name[0] in first_half_alphabet]
# # print(list_comp)
#
# resp = requests.get("http://projects.bobbelderbos.com/pcc/harry.txt")
# words = resp.text.lower().split()
#
# cnt = Counter(words)
# # print(cnt.most_common()[:5])
#
# # print('-' in words)
#
# ## Cleaning any non-alphabetical characters
# ## -- Regex: \W matches any non-alphanumeric character which is equivalent to [^a-zA-Z0-9_]
# words = [re.sub(r'\W+', r'', word) for word in words]
# # print('-' in words) ## Will print as false now
#
# resp = requests.get("http://projects.bobbelderbos.com/pcc/stopwords.txt")
# ## stopwords like "the", "about" etc
# stopwords = resp.text.lower().split()
#
# ## if word.strip() -- check if empty strings are in
# words = [word for word in words if word.strip() and word not in stopwords]
#
# cnt = Counter(words)
# print(cnt.most_common()[:5])