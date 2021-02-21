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
#
# """
# Regex -- two main methods: Search and Match
# -- match -- will match from start to end
# -- search -- can match a substring
#
# -- using raw strings (r'') in order to avoid escaping special characters like \d (digit), \w (char),
#     \s (space), \S (non-space).
# """
#
# # searching part of a string in the string saved under the text variable
# print(re.search(r'I am', text))
#
# # this will not return any result since it will do the match only end to end -- for the whole string
# print(re.match(r'I am', text))
#
# # startswith "Awesome", and ends with "challenge" -- "." -> matches any character, 0 or more of them up and until *challenge
# print(re.match(r'Awesome.*challenge', text))

"""
Compiling regexes with re.VERBOSE -- which ignores spaces and comments
"""
movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''.split('\n')

# print(movies)

#  find movie titles that have exactly 2 words
pat = re.compile(r'''
                    ^               # start of a string
                    \d+             # one or more digits
                    \.              # a literal dot
                    \s+             # one or more spaces
                    (?:             # non-capturing paranthesis, so i dont want to store this match in groups()
                    [A-Za-z']+\s    # character class (note inclusion of ' for \"Schindler's\"), followed by a space
                    )               # closing of non-capturing parenthesis
                    {2}             # exactly 2 of the previously grouped subpattern
                    \(              # literal opening parenthesis
                    \d{4}           # exactly 4 digits (year)
                    \)            # literal closing parenthesis
                    $             # end of string
                ''', re.VERBOSE)

for movie in movies:
    print(movie, pat.match(movie))