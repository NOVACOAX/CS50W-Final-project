from django import forms
from . import models

class AddWatchlist(forms.ModelForm):
    class Meta:
        model = models.Watchlist
        fields = ['user', 'text']
