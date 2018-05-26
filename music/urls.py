from django.urls import path
from . import views
app_name ="music"

urlpatterns = [
    path('', views.index, name="index"),       #blank url    http://127.0.0.1
    path('music/', views.index, name="index"),  # http://127.0.0.1/music
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/favorite', views.favorite, name='favorite'),
]
