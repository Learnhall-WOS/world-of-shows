from datetime import datetime, date

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

#general city names.. like chicago, as many venues could be in chicago... for filtering purposes
class GeneralLocation(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    

#VENUE_CHOICES = (
#    ('R', 'Renting'),
#    ('H', 'Hiring'),
#)

VENUE_STATUS = (
    ('', '............'),
    ('F', 'Free'),
    ('P', 'Paid'),
)


class Venues(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    general = models.ForeignKey(GeneralLocation, on_delete =models.CASCADE)
    name = models.TextField(max_length=250)
    slug = models.SlugField()
#    image = models.ImageField(upload_to = 'venues', null=True, blank=True)
#    choices = models.CharField(choices=VENUE_CHOICES, max_length=30, null=True, blank=True)
    location = models.TextField(max_length=250, null=True, blank=True)
    capacity = models.CharField(max_length=50, null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    fee = models.IntegerField()
    status = models.CharField(max_length=5, choices=VENUE_STATUS, default= "Free")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-fee']

    def __str__(self):
        return f"{self.name} located at {self.location}"



# users to request for renting from the detail page
class RequestRent(models.Model):
    venue  = models.ForeignKey(Venues, on_delete =models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} requested for {self.venue}"

        
