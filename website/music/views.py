from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

app_name = 'music'

def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, id):
	album = get_object_or_404(Album, pk=id)
	return render(request, 'music/detail.html', {'album': album})

def favorite(request, id):
	album = get_object_or_404(Album, pk=id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except(KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', {
			'album': album,
			'error_message': "You did not select a valid song.",
			})
	else:
		if selected_song.is_favorite:
			selected_song.is_favorite = False
		else:
			selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album': album})