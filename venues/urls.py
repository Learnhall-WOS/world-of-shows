from django.urls import path
from . import views

app_name = 'venues'



urlpatterns=[
    path('venue', views.venue_home, name= 'venue'),
    path('detail/<str:slug>', views.details, name='detail'),
    path('createvenue', views.createvenue, name='createvenue'),
    path('venue_edit/<str:id>', views.venue_edit, name='venue_edit'),
    path('remove_venue', views.remove_venue, name='remove_venue'),

]