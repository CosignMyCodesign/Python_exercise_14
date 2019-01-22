from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=50)

    def __str__(self):
        return self.artist_name

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    release_year = models.IntegerField(default=0)
    video_link = models.CharField(max_length=500, default='url')
    
    def __str__(self):
        return self.title
