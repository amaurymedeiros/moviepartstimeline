import sys

from datafetcher import DataFetcher

API_KEY = # Hidden

if len(sys.argv) == 1:
    actor_name = raw_input("Actor name: ")
else:
    actor_name = ' '.join(sys.argv[1:])

df = DataFetcher(API_KEY, actor_name)

print df.get_actor_movie_parts()