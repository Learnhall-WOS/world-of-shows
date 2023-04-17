from django.contrib import admin

# Register your models here.
from .models import Show, Genre, Review, Talent, Theater, CastMember

admin.site.register([Show, Genre, Review, Talent, Theater])

