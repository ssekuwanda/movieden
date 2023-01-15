from django.urls import path
from .views import SeriesListAPIView, SerieDetailAPIView
from . import views

urlpatterns = [
    path('', views.SeriesListAPIView.as_view(), name='series'),
    path('<int:id>', views.SerieDetailAPIView.as_view(), name="serie"),
]