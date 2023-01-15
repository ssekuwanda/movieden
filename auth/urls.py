from django.urls import path, include
from .views import SignUpAPI, SignInAPI, MainUser
from knox import views as knox_views

urlpatterns = [
    # path('api/auth/', include('knox.urls')),
    path('api/register', SignUpAPI.as_view()),
    path('api/login', SignInAPI.as_view()),
    path('api/user', MainUser.as_view()),
    path('api/logout',knox_views.LogoutView.as_view(), name="knox-logout"),
]