from rest_framework import serializers
from .models import Serie, Season, Episode

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    episode = EpisodeSerializer(source='episode_set', many=True)
    class Meta:
        model = Season
        fields = ('serie','id','season_number','episode')

class SerieSerializer(serializers.ModelSerializer):
    season = SeasonSerializer(source='season_set', many=True)
    
    class Meta:
        model = Serie
        fields = ('title','id','created','image','season')