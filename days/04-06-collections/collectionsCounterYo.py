"""
Don't reinvent the wheel, since Counter can be used
"""
from collections import Counter

words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
print(words[:5])


# Getting the most top 5 most repeated words
common_words = {}
for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] += 1

# sort dict by values descending and slice first 5 to get most common
for k, v in sorted(common_words.items(),
                   key=lambda x: x[1],
                   reverse=True)[:5]:
    print(k, v)

# Using Counter
print(f'\nNow using counter: {Counter(words).most_common(5)}')
