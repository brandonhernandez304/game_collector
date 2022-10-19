from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # video games index
    path('videogames/', views.video_games_index, name='video_games_index'),
    path('videogames/<int:video_game_id>/', views.video_games_detail, name='detail'),
    path('videogames/create/', views.VideoGameCreate.as_view(), name='video_games_create'),
    path('videogames/<int:pk>/update/', views.VideoGameUpdate.as_view(), name='video_games_update'),
    path('videogames/<int:pk>/delete/', views.VideoGameDelete.as_view(), name='video_games_delete'),
    path('videogames/<int:video_game_id>/add_playing/', views.add_playing, name='add_playing'),
    path('consoles/', views.ConsoleList.as_view(), name='consoles_index'),
    path('consoles/<int:pk>/', views.ConsoleDetail.as_view(), name='consoles_detail'),
    path('consoles/create/', views.ConsoleCreate.as_view(), name='consoles_create'),
    path('consoles/<int:pk>/update/', views.ConsoleUpdate.as_view(), name='consoles_update'),
    path('consoles/<int:pk>/delete/', views.ConsoleDelete.as_view(), name='consoles_delete'),
    path('videogames/<int:video_game_id>/assoc_console/<int:console_id>/', views.assoc_console, name='assoc_console'),
]