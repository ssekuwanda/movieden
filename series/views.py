from django.shortcuts import render
from .models import Serie
from .serializers import SerieSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class SeriesListAPIView(ListCreateAPIView):
    serializer_class = SerieSerializer
    queryset = Serie.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

class SerieDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SerieSerializer
    queryset = Serie.objects.all()
    lookup_fields = "id"