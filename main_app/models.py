from django.db import models
from django.urls import reverse

TIMES = (
    ('M', 'Morning'),
    ('D', 'Day'),
    ('N', 'Night'),
)

class Console(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('consoles_detail', kwargs={'pk': self.id})

class VideoGame(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # M:M
    consoles = models.ManyToManyField(Console)
    
    # changes to instance methods do not require re-generation / running of migrations
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'video_game_id': self.id})

class Playing(models.Model):
    date = models.DateField('Playing Date')
    time = models.CharField(
        max_length=1, 
        choices=TIMES, 
        default=TIMES[0][0]
    )

    #Create a video_game_id FK
    video_game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']

###########################################################################

# from django.db import models
# from django.urls import reverse

# TIMES = (
#     ('M', 'Morning'),
#     ('D', 'Day'),
#     ('N', 'Night'),
# )

# class Console(models.Model):
#     name = models.CharField(max_length=50)
#     color = models.CharField(max_length=50)
#     edition = models.CharField(max_length=50)

#     def get_absolute_url(self):
#         return reverse('consoles_detail', kwargs={'pk': self.id})

# class VideoGame(models.Model):
#     name = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)
#     description = models.TextField(max_length=250)
#     age = models.IntegerField()
#     # M:M
#     consoles = models.ManyToManyField(Console)
    
#     # changes to instance methods do not require re-generation / running of migrations
#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return reverse('detail', kwargs={'cat_id': self.id})

# class Playing(models.Model):
#     date = models.DateField('Playing Date')
#     time = models.CharField(
#         max_length=1, 
#         choices=TIMES, 
#         default=TIMES[0][0]
#     )

#     #Create a cat_id FK
#     videogame = models.ForeignKey(VideoGame, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.get_time_display()} on {self.date}"

#     # change the default sort
#     class Meta:
#         ordering = ['-date']