from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from PyMovieDb import IMDB
from django.db import IntegrityError
from numpy import random
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib.auth import login, logout
import json

from . import util, forms
from .models import Watchlist

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "POST":
        # Get contents of search
        data = json.loads(request.body)
        text = data.get("text", "")
        type = data.get("type", "")
        return util.search(type, text)
    else:
        imdb = IMDB()
        movies = imdb.popular_movies(genre=None, start_id=1, sort_by=None)
        Mres = json.loads(movies)
        movies = Mres['results']
        tv_shows = imdb.popular_tv(genre=None, start_id=1, sort_by=None)
        Tres = json.loads(tv_shows)
        tv_shows = Tres['results']
        Upcoming = imdb.upcoming(region=None)
        Ures = json.loads(Upcoming)
        Upcoming = Ures['results']
        Featured_id = random.randint(50)
        Featured_id = Mres['results'][Featured_id]
        Featured_id = Featured_id['id']
        featured = imdb.get_by_id(Featured_id)
        featured = json.loads(featured)
        featured['id'] = Featured_id
        return render(request, 'movies/index.html', {'movies': movies, 'tv_shows':tv_shows, 'Upcoming':Upcoming, 'featured': featured})



@csrf_exempt
def movie(request, id):
    if request.method == "POST":
        # Get contents of search
        data = json.loads(request.body)
        text = data.get("text", "")
        type = data.get("type", "")
        return util.search(type, text)
    elif request.method == "PUT":
        data = json.loads(request.body)
        if data.get("listed") ==  'no':
            user = request.user
            id = id
            Wlist = Watchlist(user=user, text=id)
            Wlist.save(force_insert=True)
            return HttpResponse(status=204)
        else:
            unlist = Watchlist.objects.get(user=request.user, text=id)
            unlist.delete()
            return HttpResponse(status=204)
    else:
        imdb = IMDB()
        movie = imdb.get_by_id(id)
        movie = json.loads(movie)
        movie['id'] = id
        movie['listed'] = util.isListed(request, id)
        movie['listed'] = movie['listed']['check']
        return render(request, 'movies/movie.html', {'movie': movie})

@csrf_exempt
def person(request, id):
    if request.method == "POST":
        # Get contents of search
        data = json.loads(request.body)
        text = data.get("text", "")
        type = data.get("type", "")
        return util.search(type, text)
    else:
        imdb = IMDB()
        Sid = util.stripid(id)
        person = imdb.person_by_id(Sid)
        person = json.loads(person)
        person['id'] = Sid
        return render(request, 'movies/person.html', {'person': person})

@csrf_exempt
def search(request):
    # Search must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    # Get contents of search
    text = data.get("text", "")
    type = data.get("type", "")

    imdb = IMDB()
    if type == "person":
        search = imdb.search(text, year=None, tv=False, person=True)
    elif type == "tv":
        search = imdb.search(text, year=None, tv=True, person=False)
    else :
        search = imdb.search(text, year=None, tv=False, person=False)
    res = json.loads(search)
    print(res)
    return JsonResponse(res)

@login_required
@csrf_exempt
def list(request):
    if request.method == "POST":
        # Get contents of search
        data = json.loads(request.body)
        text = data.get("text", "")
        type = data.get("type", "")
        return util.search(type, text)
    else:
        imdb = IMDB()
        moviesL = Watchlist.objects.filter(user=request.user).order_by('timestamp').all()
        movies = []
        for id in moviesL:
            id = str(id)
            content = imdb.get_by_id(id)
            content = json.loads(content)
            content['id'] = id
            movies.append(content)

        return render(request, 'movies/list.html', {'movies': movies})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("movies/")
    else:
        form = UserCreationForm()
    return render(request, 'movies/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect("movies/")
    else:
        form = AuthenticationForm()
    return render(request, 'movies/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("movies/")