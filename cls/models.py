from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.

class ClassUser(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_instructor = models.BooleanField(default=False)

class Class(models.Model): 
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(ClassUser, on_delete=models.CASCADE, related_name="owner")
    instructor = models.ManyToManyField(ClassUser)
    description = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    schedule = models.CharField(max_length=100)

    def schedule_checker(self,schedule_str): 
        days_in_a_week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        schedules = schedule_str.split(",")
        if self.start_date.strftime("%A").lower() not in days_in_a_week : 
            raise ValidationError("Your start date should be included into your schedule")
        for day in schedules: 
            if day.lower() not in days_in_a_week: 
                raise ValidationError("Please check the spelling of your days in a week, also be careful not to use whitespaces between commas")
    
    def check_inputs(self):
        if not self.owner.is_instructor : 
            raise ValidationError ("owner must be an instructor")
        for instructor in self.instructor_set.all(): 
            if not instructor.is_instructor : 
                raise ValidationError("Non Instructor user cannot become an instructor!")
        if (self.end_date < self.start_date or self.start_date < datetime.now().date()) : 
            raise ValidationError("You cannot set the end date < start date or start date < today")
        self.schedule_checker(self.schedule)
            

    def save(self, *args, **kwargs): 
        self.check_inputs()
        super(Class,self).save(*args,**kwargs)
        






