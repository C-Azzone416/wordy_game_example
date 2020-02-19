from django.urls import path

from wordy_game_app.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register', Register.as_view(), name='register'),
]
