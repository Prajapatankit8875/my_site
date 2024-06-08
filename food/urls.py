from django.urls import path
from food.views import hello

urlpatterns = [
    path('hello/', hello),
]