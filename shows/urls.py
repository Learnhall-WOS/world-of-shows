from django.urls import path
from . import views

urlpatterns = [

    path('shows/', views.home_shows, name='home-shows'),

    path('show/<str:pk>/', views.shows, name='show'),
    path('post-show/', views.post_show, name="post-show"),
    path('update-show/<str:pk>/', views.update_show, name="update-show"),
    path('delete-show/<str:pk>/', views.delete_show, name="delete-show"),

    path('profile/<str:pk>/', views.user_profile, name='user-profile'),

]