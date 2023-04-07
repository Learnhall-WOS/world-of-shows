from django.contrib import admin

# Register your models here.
from .models import Show, Genre, Review, Talent, Theater

admin.site.register([Show, Genre, Review, Talent, Theater])

