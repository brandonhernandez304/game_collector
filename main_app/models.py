from django.db import models
from django.urls import reverse


TIMEPLAYED = (
    ('M', 'Morning'),
    ('D', 'Day'),
    ('N', 'Night'),
)
# Consoles go here
class Console(models.Model):
    name = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('consoles_detail', kwargs={'pk':self.id})
    

class VideoGame(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # M:M goes here, gonna be consoles
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'video_game_id':self.id})




videogames = [
    VideoGame('The Last of Us 2', 'survival', 'awesome gameplay', 2),
    VideoGame('God of War', 'action', 'boy', 4),
]


class Meta:
    ordering = ['-date']