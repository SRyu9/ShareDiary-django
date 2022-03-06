from django.urls import path
from .views import profilefunction

urlpatterns = [
    path('profile/',  profilefunction),
]
