import csv
from collections import namedtuple, defaultdict
from urllib.request import urlretrieve
from collections import Counter


movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'

urlretrieve(movie_data, movies_csv)

# adding named tuple -- first argument is the name of the object,
# second are the elements it will contain
Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors

directors = get_movies_by_director()
# print(directors)

cnt = Counter()
print(type(cnt))
for director, movies in directors.items():
    cnt[director] += len(movies)

print(cnt.most_common(5))