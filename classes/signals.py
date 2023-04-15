from django.db.models.signals import post_save,m2m_changed, pre_save
from django.dispatch import receiver
from .models import Class, ClassUser
from django.core.exceptions import ValidationError
from datetime import datetime

""" These signals are mainly used to handle input validation of models. This is useful to handle non-form origin inputs such as direct input from admin page or using shell """

def schedule_checker(instance,schedule_str): 
        """helper method to check whether the string inputs can be converted into date object and be evaluated"""
        days_in_a_week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        schedules = schedule_str.split(",")
        if instance.start_date.strftime("%A").lower() not in schedules : 
            raise ValidationError("Your start date should be included into your schedule")
        for day in schedules: 
            if day.lower() not in days_in_a_week: 
                raise ValidationError("Please check the spelling of your days in a week, also be careful not to use whitespaces between commas")
    
def check_inputs(instance,*args,**kwargs):
        """helper method to check inputs from source other than form ( for example : create object from shell ) """

        if not instance.owner.is_instructor : 
            raise ValidationError ("owner must be an instructor")
        
        if (instance.end_date < instance.start_date or instance.start_date < datetime.now().date()) : 
            raise ValidationError("You cannot set the end date < start date or start date < today")
            
        schedule_checker(instance,instance.schedule) 






@receiver(m2m_changed, sender=Class.instructor.through)
def check_instructor_status(sender,instance,action,**kwargs): 

    if action=="pre_add" : 
        pk_set=kwargs.pop('pk_set',None)
        if pk_set : 
            instructor_list = ClassUser.objects.filter(id__in=pk_set)
            for instructor in instructor_list : 
                if not instructor.is_instructor: 
                    raise ValidationError("Only can add ClassUser with the property of is_instructor equal to True")

@receiver(pre_save,sender=Class)
def sanitize_inputs(sender,instance,*args,**kwargs):
     print("This message is from signal")
     check_inputs(instance)
