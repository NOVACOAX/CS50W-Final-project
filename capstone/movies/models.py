from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    text = models.CharField(max_length=12,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text