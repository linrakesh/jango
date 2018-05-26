# from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album,song

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
    # try:
    #     album = Album.objects.get(pk=id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist...Try again")
    album = get_object_or_404(Album,pk=id)
    return render(request,'music/detail.html',{'album':album})

def favorite(request,id):
    album = get_object_or_404(Album,pk=id)
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except (KeyError,song.DoesNotExist):
        return(request,'music/detail.html',{'album':album,'error_message':"You did not selected a valid song"})
    else:
        if selected_song.is_favorite:
            selected_song.is_favorite = False
        else:
            selected_song.is_favorite = True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})
