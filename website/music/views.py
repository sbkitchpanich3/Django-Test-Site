from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album

def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, id):
	album = get_object_or_404(Album, pk=id)
	return render(request, 'music/detail.html', {'album': album})