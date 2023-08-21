from PyMovieDb import IMDB
from django.http import JsonResponse
import json

from .models import Watchlist


def popularMovies():
    imdb = IMDB()
    movies = imdb.popular_movies(genre=None, start_id=1, sort_by=None)
    Mres = json.loads(movies)
    movies = Mres['results']
    movieList = []
    for movie in movies:
        Mid = movie['id']
        content = imdb.get_by_id(Mid)
        movieList.append(content)

    return movieList

def stripid(id):
    text = id 
    text = text.split("/")
    return text[2]

def search(type, text):
    imdb = IMDB()
    if type == "person":
        search = imdb.search(text, year=None, tv=False, person=True)
    elif type == "tv":
        search = imdb.search(text, year=None, tv=True, person=False)
    else :
        search = imdb.search(text, year=None, tv=False, person=False)
    res = json.loads(search)
    return JsonResponse(res)

def isListed(request, id):
    user = request.user
    check = Watchlist.objects.filter(user=user, text=id).count()
    if check == 0:
        return {"check": False}
    else:
        return {"check": True}
