from django.http import HttpResponse
from django.template import loader
from .models import Album

def index(request):
    all_album = Album.objects.all()
    # html ='<ul>'
    # for album in all_album:
    #     html = html+"<li><a href='/"+str(album.id)+ "'>"+ album.artist +" </a></li>"
    # html +='</ul>'
    template = loader.get_template('music/index.html')
    context = {'all_album':all_album}
    return HttpResponse(template.render(context,request))

def home(request,id):
    return HttpResponse("This is home page"+str(id))