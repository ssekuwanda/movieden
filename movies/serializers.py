from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description','image','file', )
        model = Movie

class UpcomingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title','image',)
        model = Upcoming

class DownloadedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user', 'movie' )
        model = Downloaded

class QrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCodePayment
        fields = ('id','code','user','amount','timestamp','used')