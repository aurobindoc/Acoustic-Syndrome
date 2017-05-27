from django.http import HttpResponse
from .models import Artist


def index(request):
    all_artist = Artist.objects.all()
    html = ''
    for artist in all_artist:
        url = '/guitar/' + str(artist.id) + "/"
        html += '<a href="' + url + '">' + artist.name + '</a><br>'
    return HttpResponse(html)


def detail(request, artist_id):
    return HttpResponse("<h2>Artist ID = " + str(artist_id) + "</h1>")