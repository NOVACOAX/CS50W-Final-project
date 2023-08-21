from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
app_name = 'movies'

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.signup_view, name="register"),
    path("movie/<str:id>", views.movie, name="movie"),
    path("people<path:id>", views.person, name="people"),
    path("search", views.search, name="search"),
    path("list", views.list, name="list")
]

urlpatterns += staticfiles_urlpatterns()