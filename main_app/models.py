from django.db import models

# Create your models here.
class VideoGame:
    def __init__(self, name, genre, description, age):
        self.name = name
        self.genre = genre
        self.description = description
        self.age = age


videogames = [
    VideoGame('The Last of Us 2', 'survival', 'awesome gameplay', 2),
    VideoGame('God of War', 'action', 'boy', 4),
]