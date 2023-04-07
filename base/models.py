from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Theater(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # address = 
    # contact = 
    # email =
    # Add any other relevant fields for a theater here

    def __str__(self) -> str:
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
class Talent(models.Model):
    name = models.CharField(max_length=100)
    # contact = 
    # email =
    
    def __str__(self):
        return self.name
    

class Show(models.Model):
    name = models.CharField(max_length=200)
    host = models.ForeignKey(Theater, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    talent = models.ManyToManyField(Talent, blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self) -> str:
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if not self.host_id:
            self.host_id = self.user.theater.id
        super(Show, self).save(*args, **kwargs)
    

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    text = models.TextField()
    #rating = models.IntegerField(choices=RATING_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self) -> str:
        return self.text[0:50] 