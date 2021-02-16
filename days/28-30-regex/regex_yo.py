import re

"""
When not to use regex
"""
text = "Awesome, I am doing the #100DaysOfCode challenge"

# # Does the text start with "Awesome"?
# print(text.startswith("Awesome"))
#
# # Or does it end with challenge?
# print(text.endswith("challenge"))
#
# # Does the text contain "100daysofcode" (case insensitive)?
# print("100daysofcode" in text.lower())
#
# # Replace 100 with 200 days of code
# print(text.replace("100", "200"))

"""
Regex -- two main methods: Search and Match
-- match -- will match from start to end
-- search -- can match a substring

-- using raw strings (r'') in order to avoid escaping special characters like \d (digit), \w (char),
    \s (space), \S (non-space). 
"""

# # searching part of a string in the string saved under the text variable
# print(re.search(r'I am', text))
#
# # this will not return any result since it will do the match only end to end -- for the whole string
# print(re.match(r'I am', text))
#
# # startswith "Awesome", and ends with "challenge" -- "." -> matches any character, 0 or more of them up and until *challenge
# print(re.match(r'Awesome.*challenge', text))

"""
String capturing paranthesis
"""
# hundred = 'Awesome, I am doing the #100DaysOfCode challenge'
#
# # \d --means one or more digits
# m_search = re.search(r'(#\d+DaysOfCode)', hundred)
# print(m_search)
# print(f'Printing m_search.groups(): {m_search.groups()[0]}')
#
# # when trying to use match for the whole string to be matched:
# # .* --accounts for anything that comes before/after
# m_match = re.match(r'.*(#\d+DaysOfCode).*', hundred)
# print(m_match)
# print(f'Printing m_match.groups: {m_match.groups()}')
# print(f'Printing m_match.groups and getting the actual string: {m_match.groups()[0]}')

"""
findall
"""
text = """
$ python module_index.py |grep ^re
re                  | stdlib | 005, 007, 009, 015, 021, 022, 068, 081, 086, 095
"""
# print(re.findall(r'\d+', text))

text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been ,
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and ,
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into ,
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of,
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus,
PageMaker including versions of Lorem Ipsum
"""
# '\w+' --extracting words
# '\w' --extracting characters --or you can use text.split() to get the same output
# print(re.findall(r'\w+', text))

# find the most common words that start with an upper-case letter
# [a-z0-9] --means one or more lowercase characters or digits
# + --means one or more
from collections import Counter
cnt = Counter(re.findall(r'[A-Z][a-z0-9]+', text))
print(cnt)
print(cnt.most_common(5))


