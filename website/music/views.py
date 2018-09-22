from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>FUCKWAD</h1>")

def detail(request, id):
	return HttpResponse("<h2>Details for Album ID: " + str(id) + "</h2>")