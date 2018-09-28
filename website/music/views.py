from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, id):
	try:
		album = Album.objects.get(pk=id)
	except Album.DoesNotExist:
		raise Http404("FUCK OUTTA HERE WITH THAT MISSING ALBUM SHIT")
	return render(request, 'music/detail.html', {'album': album})