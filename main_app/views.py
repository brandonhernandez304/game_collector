from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Game, Console
from .forms import PlayingForm


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request,"about.html")

# games #

def games_index(request):
    games = Game.objects.filter(user=request.user)
    return render(request, 'games/index.html', {'games': games })


@login_required
def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    playing_form = PlayingForm()
    # displaying unassociated consoles
    consoles_game_doesnt_have = Console.objects.exclude(id__in = game.consoles.all().values_list('id'))
    return render(request, 'games/detail.html', {
    # include the cat and playing_form in the context
    'game': game,
    'playing_form': playing_form,
    'consoles' : consoles_game_doesnt_have,
  })

@login_required
def add_playing(request, game_id):
    form = PlayingForm(request.POST)
    if form.is_valid():
        new_playing = form.save(commit=False)
        new_playing.game_id = game_id
        new_playing.save()
    return redirect('detail', game_id=game_id)

@login_required
def assoc_console(request, game_id, console_id):
  # Note that you can pass a console's id instead of the whole object
   Game.objects.get(id=game_id).consoles.add(console_id)
   return redirect('detail', game_id=game_id)
# consoles #

# CBV's
class GameCreate(LoginRequiredMixin,CreateView):
    model = Game
    fields = ['name', 'genre', 'description', 'age']
    # success_url= '/games/'
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the game
    # Let the CreateView do its job as usual
        return super().form_valid(form)


class GameUpdate(LoginRequiredMixin,UpdateView):
    model = Game
    fields = ['name', 'genre', 'description', 'age']

class GameDelete(LoginRequiredMixin,DeleteView):
    model = Game
    success_url = '/games/'

# Consoles #
class ConsoleCreate(LoginRequiredMixin,CreateView):
    model = Console
    fields = ('name', 'color', 'edition')
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the console
    # Let the CreateView do its job as usual
        return super().form_valid(form)

class ConsoleUpdate(LoginRequiredMixin,UpdateView):
    model = Console
    fields = ('name', 'color')

class ConsoleDelete(LoginRequiredMixin,DeleteView):
    model = Console
    success_url = '/consoles/'

class ConsoleDetail(LoginRequiredMixin,DetailView):
    model = Console
    template_name = 'consoles/detail.html'


    
def consoles_index(request):
    consoles = Console.objects.filter(user=request.user)
    return render(request, 'consoles/index.html', {'consoles': consoles })



#################################################################
# Signup code, just google or look at md for reference
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


# Create your views here.
# def home(request):
#     return render(request, 'home.html')

# def about(request):
#     return render(request, 'about.html')

# def games_index(request):
#     games = Game.objects.all()
#     return render(request, 'games/index.html', {'games':games})

# # update this view function
# def games_detail(request, game_id):
#   game = Game.objects.get(id=game_id)
#   # instantiate PlayingForm to be rendered in the template
#   playing_form = PlayingForm()
 
#   # displaying unassociated consoles
#   consoles_game_doesnt_have = Console.objects.exclude(id__in = game.consoles.all().values_list('id'))
#   return render(request, 'games/detail.html', {
#     # including the game and playing form 
#     'game': game,
#     'playing_form': playing_form,
#     'consoles' : consoles_game_doesnt_have,
#   })

# def add_playing(request, game_id):
#     form = PlayingForm(request.POST)
#     if form.is_valid():
#         new_playing = form.save(commit=False)
#         new_playing.game_id = game_id
#         new_playing.save()
#     return redirect('detail', game_id=game_id)
    
# def assoc_console(request, game_id, console_id):
#   # Note that you can pass a console's id instead of the whole object
#    Game.objects.get(id=game_id).consoles.add(console_id)
#    return redirect('detail', game_id=game_id)

# class GameCreate(CreateView):
#     model = Game
#     fields = ['name','genre','description','age']
#     success_url = '/games/' 

# class GameUpdate(UpdateView):
#     model = Game
#     fields = ('genre', 'description', 'age')

# class GameDelete(DeleteView):
#     model = Game
#     success_url = '/games/'

# class ConsoleCreate(CreateView):
#     model = Console
#     fields = ('name', 'color', 'edition')

# class ConsoleUpdate(UpdateView):
#     model = Console
#     fields = ('name', 'color', 'edition')

# class ConsoleDelete(DeleteView):
#     model = Console
#     success_url = '/consoles/'

# class ConsoleDetail(DetailView):
#     model = Console
#     template_name = 'consoles/detail.html'

# class ConsoleList(ListView):
#     model = Console
#     template_name = 'consoles/index.html'
