from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
from .models import Class, ClassUser
from django.core.exceptions import ValidationError

@receiver(m2m_changed, sender=Class.instructor.through)
def check_instructor_status(sender,instance,action,**kwargs): 

    if action=="pre_add" : 
        pk_set=kwargs.pop('pk_set',None)
        if pk_set : 
            instructor_list = ClassUser.objects.filter(id__in=pk_set)
            for instructor in instructor_list : 
                if instructor.is_instructor: 
                    print(str(instructor))
        # print(instructor_list)
        # for ins in instructor_list : 
        #     if not ins.is_instructor: 
        #         instance.instructor.clear()             
        #         raise ValidationError("Instructors cannot contain a non Instructor user, the instructor value will be set to Null") 
