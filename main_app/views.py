from django.shortcuts import render, redirect

from main_app.models import VideoGame

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def video_game_index(request):
    videogames = VideoGame.objects.all()
    return render(request, 'videogames/index.html', {'videogames':videogames})