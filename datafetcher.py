import json
import sys
from urllib2 import Request, urlopen

from entities import Actor, Movie, MoviePart


class DataFetcher():
    DEFAULT_HEADERS = {'Accept': 'application/json'}
    TVDB_API_URL = 'http://api.themoviedb.org/3/'

    def __init__(self, api_key, actor_name):
        self._request_suffix = '&api_key=%s' % api_key
        self._actor = self._query_actor(actor_name)

    def _query_actor(self, name):
        query = name.replace(' ', '+')
        actor_data = self._get_json_response('search/person?query=%s' % query)
        try:
            if int(actor_data['total_results']) > 0:
                actor = actor_data['results'][0]
                return Actor(actor['id'], actor['name'])            
        except KeyError:
            print 'Invalid response. Actor not found. Please try again.'
            sys.exit(1)

    def get_actor_movie_parts(self):
        movie_parts = []
        credits = self._get_json_response(
            'person/%s/movie_credits' % self._actor.get_id(), True)
        movie_list = credits['cast']
        for entry in movie_list:
            # TODO: avoid querying the movie rating every time
            movie = Movie(entry['id'], entry['title'], entry['release_date'],
                          self._get_movie_rating(entry['id']))
            movie_parts.append(MoviePart(movie, entry['character']))
        return movie_parts

    def _get_movie_rating(self, movie_id):
        movie = self._get_json_response('movie/%s' % movie_id, True)
        return movie['vote_average']

    def _debug_print_movie_parts(self, movie_parts):
        for part in movie_parts:
            if not part.is_future_part():
                print '%s (%s)' % (part.get_movie_title(), part.get_movie_year())
                print 'Character: %s' % part.get_character_name()
                print 'Rating: %s' % part.get_movie_rating()
                print

    def _get_json_response(self, url_data, single_param=False):
        request_url = '%s%s%s' % (self.TVDB_API_URL, url_data, 
                                  self._request_suffix)
        if single_param:
            request_url = request_url.replace('&', '?')
        request = Request(request_url, headers = self.DEFAULT_HEADERS)
        return json.loads(urlopen(request).read())