from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Album

def index(request):
    all_album = Album.objects.all()
    # html ='<ul>'
    # for album in all_album:
    #     html = html+"<li><a href='/"+str(album.id)+ "'>"+ album.artist +" </a></li>"
    # html +='</ul>'
    # template = loader.get_template('music/index.html')

    # context = {'all_album':all_album}
    return render(request,'music/index.html',{'all_album':all_album})

def detail(request,id):
    try:
        album = Album.objects.get(pk=id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist...Try again")
    return render(request,'music/detail.html',{'album':album})