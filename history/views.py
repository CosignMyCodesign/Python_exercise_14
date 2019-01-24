from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Artist, Song

# Create your views here.


def index(request):
    latest_artist_list = Artist.objects.all()
    context = {'latest_artist_list': latest_artist_list}
    return render(request, 'history/index.html', context)

def views(request, artist_name):
    return HttpResponse(f"You're looking at the artists {artist_name}.")

def detail(request, artist_id):
    latest_song_list = Song.objects.filter(artist_id=artist_id)
    context = {'latest_song_list': latest_song_list}
    return render(request, 'history/detail.html', context)

def addArtistForm(request):
    return render(request, 'history/form.html')

def postartist(request):
   
    artist = request.POST['artist']
    newArtist = Artist(artist_name= artist)
    print("my newly submitted artist", newArtist)
    newArtist.save()

    return HttpResponseRedirect(reverse('history:detail', args=(newArtist.id,)))
