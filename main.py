import os
import sys

from dotenv import load_dotenv

from datafetcher import DataFetcher

DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)

if len(sys.argv) == 1:
    actor_name = raw_input('Actor name: ')
else:
    actor_name = ' '.join(sys.argv[1:])

df = DataFetcher(os.environ.get('API_KEY'), actor_name)

print df.get_actor_movie_parts()