from django.shortcuts import render
from django.http import HttpResponse
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

# def song_detail(request, song_id)
#     song_detes = Song.objects.filter(song_id=song_id)
#     context = {'song_detes': song_detes}
#     return render(request, 'history/song_detail.html', context)