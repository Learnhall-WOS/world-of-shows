from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime
from django.conf import settings
import os

# Create your models here.

class ClassUser(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_instructor = models.BooleanField(default=False)

    def __str__(self): 
        return f"{self.id}--{self.user.username}--{self.is_instructor}"

class Class(models.Model): 

    def upload_path(instance,filename): 
        now = datetime.now().date().strftime("%Y-%m-%d")
        filename = filename[:50]
        filename += f"-{now}"
        path = os.path.join(settings.CLASSES_UPLOADED_FOLDER,filename)
        return path

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(ClassUser, on_delete=models.CASCADE, related_name="owner")
    instructor = models.ManyToManyField(ClassUser,null=True,blank=True)
    description = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    schedule = models.CharField(max_length=100)
    image = models.FileField(upload_to=upload_path,null=True,blank=True)
    
    def __str__(self) :
        return f"{self.id}--{self.name}"
        
    # Input Validation of this models are handled by pre_save and m2m_changed signals 





