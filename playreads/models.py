from django.db import models
import uuid

# Create your models here.
class Play(models.Model):
    play_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # play_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name