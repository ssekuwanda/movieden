from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from uuid import uuid4
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import random
import string

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name="moviegenre")
    slug = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="Cover Images", null=True)
    file = models.FileField(upload_to="Video", null=True)
    created = models.DateField(null=False, blank=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify('{} {}'.format(self.title, str(uuid4())))
        super(Movie, self).save(*args, **kwargs)

class Upcoming(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to="Cover Images", null=False, blank=False)
    created = models.DateField(null=False, blank=False, auto_now_add=True)

    def __str__(self):
        return self.title

class Downloaded(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    movie = models.ManyToManyField(Movie, related_name='my_movies', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user']

class QrCodePayment(models.Model):
    code = models.CharField(max_length=700, blank=True, null=False)
    user = models.ForeignKey(User, related_name='payer', blank=True, null=True, on_delete=models.SET_NULL)
    creator = models.ForeignKey(User, related_name='issuer',blank=True, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    password = models.CharField(max_length=100, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return str(self.amount)

    def save(self, *args, **kwargs):
        klass = self.__class__
        if self.code:
            new_code = self.code
        else:
            new_code = ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(107))
            if klass.objects.filter(code=new_code).exists():
                new_code = ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(107))
            self.code = new_code
        super(QrCodePayment, self).save(*args, **kwargs)

class SaleSummary(QrCodePayment):
    class Meta:
        proxy = True
        verbose_name = 'Sale Summary'
        verbose_name_plural = 'Sales Summary'

