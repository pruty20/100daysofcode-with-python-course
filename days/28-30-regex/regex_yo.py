import re

"""
When not to use regex
"""
text = "Awesome, I am doing the #100DaysOfCode challenge"

# Does the text start with "Awesome"?
print(text.startswith("Awesome"))

# Or does it end with challenge?
print(text.endswith("challenge"))

# Does the text contain "100daysofcode" (case insensitive)?
print("100daysofcode" in text.lower())

# Replace 100 with 200 days of code
print(text.replace("100", "200"))

"""
Regex -- two main methods: Search and Match
-- match -- will match from start to end
-- search -- can match a substring

-- using raw strings (r'') in order to avoid escaping special characters like \d (digit), \w (char),
    \s (space), \S (non-space). 
"""

# searching part of a string in the string saved under the text variable
print(re.search(r'I am', text))

# this will not return any result since it will do the match only end to end -- for the whole string
print(re.match(r'I am', text))

# startswith "Awesome", and ends with "challenge" -- "." -> matches any character, 0 or more of them up and until *challenge
print(re.match(r'Awesome.*challenge', text))