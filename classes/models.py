from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.

class ClassUser(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_instructor = models.BooleanField(default=False)

    def __str__(self): 
        return f"{self.id}--{self.user.username}--{self.is_instructor}"

class Class(models.Model): 
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(ClassUser, on_delete=models.CASCADE, related_name="owner")
    instructor = models.ManyToManyField(ClassUser,null=True,blank=True)
    description = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    schedule = models.CharField(max_length=100)
    
    def __str__(self) :
        return f"{self.id}--{self.name}"
        
    # Input Validation of this models are handled by pre_save and m2m_changed signals 





