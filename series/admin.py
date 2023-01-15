from django.contrib import admin
from .models import Serie, Season, Episode

class SeasonInline(admin.TabularInline):
    model = Season

class SerieAdmin(admin.ModelAdmin):
    inlines = [
        SeasonInline,
    ]

class EpisodeInline(admin.TabularInline):
    model = Episode

class SeasonAdmin(admin.ModelAdmin):
    inlines = [
        EpisodeInline,
    ]

admin.site.register(Serie,SerieAdmin)
admin.site.register(Season, SeasonAdmin)
