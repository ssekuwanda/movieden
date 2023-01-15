from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesListAPIView.as_view(), name='movies'),
    path('<int:id>', views.MovieDetailAPIView.as_view(), name="movie"),
    path('upcoming', views.UpcomingListAPIView.as_view(), name="upcoming"),
    path('qr/', views.qrcode_generation, name="qrcode_generation"),
    path('qr/<slug:slug>', views.gen_code, name="qrcode"),
    path('qr_list', views.qr_list, name="qr_list"),
    path('qr/update/<int:pk>', views.update_qr, name="update_qr"),
]

