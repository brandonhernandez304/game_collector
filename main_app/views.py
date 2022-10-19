from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import VideoGame, Console
from .forms import PlayingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def video_games_index(request):
    video_games = VideoGame.objects.all()
    return render(request, 'videogames/index.html', {'videogames':video_games})

# update this view function
def video_games_detail(request, video_game_id):
  video_game = VideoGame.objects.get(id=video_game_id)
  # instantiate PlayingForm to be rendered in the template
  playing_form = PlayingForm()

  # displaying unassociated consoles
  consoles_video_game_doesnt_have = Console.objects.exclude(id__in = video_game.consoles.all().values_list('id'))

  return render(request, 'videogames/detail.html', {
    # including the video_game and playing form
    'video_game': video_game,
    'playing_form': playing_form,
    'consoles' : consoles_video_game_doesnt_have,
  })

def add_playing(request, video_game_id):
    form = PlayingForm(request.POST)
    if form.is_valid():
        new_playing = form.save(commit=False)
        new_playing.video_game_id = video_game_id
        new_playing.save()
    return redirect('detail', video_game_id=video_game_id)

def assoc_console(request, video_game_id, console_id):
  # Note, can pass a console's id instead of the whole object
   VideoGame.objects.get(id=video_game_id).consoles.add(console_id)
   return redirect('detail', video_game_id=video_game_id)

class VideoGameCreate(CreateView):
    model = VideoGame
    fields = ['name','genre','description','age']
    success_url = '/videogames/' 

class VideoGameUpdate(UpdateView):
    model = VideoGame
    fields = ('genre', 'description', 'age')

class VideoGameDelete(DeleteView):
    model = VideoGame
    success_url = '/videogames/'

class ConsoleCreate(CreateView):
    model = Console
    fields = ('name', 'color', 'edition')

class ConsoleUpdate(UpdateView):
    model = Console
    fields = ('name', 'color', 'edition')

class ConsoleDelete(DeleteView):
    model = Console
    success_url = '/consoles/'

class ConsoleDetail(DetailView):
    model = Console
    template_name = 'consoles/detail.html'

class ConsoleList(ListView):
    model = Console
    template_name = 'consoles/index.html'
