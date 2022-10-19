from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # video games index
    path('videogames/', views.video_games_index, name='index'),
]