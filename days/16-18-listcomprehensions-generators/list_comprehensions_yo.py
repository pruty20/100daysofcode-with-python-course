from collections import Counter
import calendar, itertools, random, re, string, requests

names = "pybites mike bob julian tim sara guido".split()

# for name in names:
#     print(name.title())

first_half_alphabet = list(string.ascii_lowercase)[:13]
# print(first_half_alphabet)

new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())
# print(new_names)

## List Comprehensions
list_comp = [name.title() for name in names if name[0] in first_half_alphabet]
# print(list_comp)

resp = requests.get("http://projects.bobbelderbos.com/pcc/harry.txt")
words = resp.text.lower().split()

cnt = Counter(words)
# print(cnt.most_common()[:5])

# print('-' in words)

## Cleaning any non-alphabetical characters
## -- Regex: \W matches any non-alphanumeric character which is equivalent to [^a-zA-Z0-9_]
words = [re.sub(r'\W+', r'', word) for word in words]
# print('-' in words) ## Will print as false now

resp = requests.get("http://projects.bobbelderbos.com/pcc/stopwords.txt")
## stopwords like "the", "about" etc
stopwords = resp.text.lower().split()

## if word.strip() -- check if empty strings are in
words = [word for word in words if word.strip() and word not in stopwords]

cnt = Counter(words)
print(cnt.most_common()[:5])