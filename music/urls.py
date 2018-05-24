from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),       #blank url    http://127.0.0.1
    path('music/', views.index, name="index"),  # http://127.0.0.1/music
    path('<int:id>/', views.detail, name='detail'),
]
