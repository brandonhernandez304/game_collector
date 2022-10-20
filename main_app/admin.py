from django.contrib import admin
from .models import VideoGame, Playing, Console
# Register your models here.

admin.site.register(VideoGame)
admin.site.register(Playing)
admin.site.register(Console)