from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def video_game_index(request):
    return render(request, 'videogames/index.html', {'videogames':videogames})