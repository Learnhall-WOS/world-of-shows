from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_play_reads, name='home_play_reads'),
    path('play/<uuid:play_id>/', views.play_detail, name='play_detail'),
    path('play/<uuid:play_id>/participate/', views.participate, name='participate'),
]