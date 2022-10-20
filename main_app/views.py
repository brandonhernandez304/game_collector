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

def games_index(request):
    games = VideoGame.objects.all()
    return render(request, 'videogames/index.html', {'games':games})

# update this view function
def games_detail(request, game_id):
  game = VideoGame.objects.get(id=game_id)
  # instantiate PlayingForm to be rendered in the template
  playing_form = PlayingForm()
 
  # displaying unassociated consoles
  consoles_game_doesnt_have = Console.objects.exclude(id__in = game.consoles.all().values_list('id'))

  return render(request, 'videogames/detail.html', {
    # including the game and playing form 
    'game': game,
    'playing_form': playing_form,
    'consoles' : consoles_game_doesnt_have,
  })
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

def add_playing(request, game_id):
    form = PlayingForm(request.POST)
    if form.is_valid():
        new_playing = form.save(commit=False)
        new_playing.game_id = game_id
        new_playing.save()
    return redirect('detail', game_id=game_id)
    
def assoc_console(request, game_id, console_id):
  # Note, can pass a console's id instead of the whole object
   VideoGame.objects.get(id=game_id).consoles.add(console_id)
   return redirect('detail', game_id=game_id)