from django.db import models
from django.contrib.auth.models import (PermissionsMixin, AbstractBaseUser, BaseUserManager)

class Serie(models.Model):
    title = models.CharField(max_length=300)
    created = models.DateField(null=False, blank=False, auto_now_add=True)
    image = models.ImageField(upload_to="Cover Images", null=True)

    def __str__(self):
        return self.title

class Season(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    season_number = models.PositiveIntegerField()
    created = models.DateField(null=False, blank=False, auto_now_add=True)

    def __str__(self):
        return str(self.serie) + ' ' + 'S' + str(self.season_number)
        

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    episode_number = models.PositiveIntegerField()
    created = models.DateField(null=False, blank=False, auto_now_add=True)
    file = models.FileField(upload_to="Video", null=True)

    def __str__(self):
        return str(self.season.serie.title) + 'E' + str(self.episode_number)
        
        