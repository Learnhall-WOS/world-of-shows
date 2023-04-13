from django.test import TestCase 
from cls.models import Class,ClassUser
from django.contrib.auth.models import User
from datetime import datetime, timedelta, time
from django.core.exceptions import ValidationError

class TestClassTestCase(TestCase): 
    @classmethod
    def setUpClass(cls): 
        super().setUpClass()
        User.objects.create(username="user1",password="strongpassword123")
        User.objects.create(username="user2",password="strongpassword123")
        User.objects.create(username="user3",password="strongpassword123")
        User.objects.create(username="user4",password="strongpassword123")
        User.objects.create(username="user5",password="strongpassword123")
        User.objects.create(username="user6",password="strongpassword123")
    
    def setUp(self): 
        users = User.objects.all() 
        for i,user in enumerate(users):
            if i%2 == 0 : 
                ClassUser.objects.create(user=user,is_instructor=True)
            else : 
                ClassUser.objects.create(user=user)
        
        self.instructor_list = [x for x in ClassUser.objects.all() if x.is_instructor]
        self.good_owner = ClassUser.objects.get(id=1)
        self.bad_owner = ClassUser.objects.get(id=2)
        self.good_start_date = datetime.now().date() + timedelta(days=2)
        self.good_end_date = datetime.now().date() + timedelta(days=10)
        self.bad_start_date = datetime.now().date() + timedelta(days=-1)
        self.bad_end_date = datetime.now().date() + timedelta(days=-1)
        schedules = [self.good_start_date, self.good_start_date + timedelta(days=1)]
        good_schedule_list = [x.strftime("%A").lower() for x in schedules]
        self.good_schedule = ",".join(good_schedule_list)
        self.bad_schedule = self.bad_start_date.strftime("%A").lower()

        Class.objects.create(
            name="Class one",
            owner=self.good_owner,
            description="The master class to master art",
            start_date = self.good_start_date,
            end_date = self.good_end_date,
            start_time = time(9,30,0),
            end_time = time(14,0,0),
            schedule = self.good_schedule
        )
        self.class1 = Class.objects.get(id=1)
        for instructor in self.instructor_list: 
            self.class1.instructor.add(instructor)

    def test_object_str_repr(self): 
        self.assertEqual(str(self.class1),"1--Class one")

    def test_owner_not_an_instructor(self): 
        with self.assertRaisesMessage(ValidationError,"['owner must be an instructor']"):
            Class.objects.create(
            name="Class two",
            owner=self.bad_owner,
            description="The master class to master art",
            start_date = self.good_start_date,
            end_date = self.good_end_date,
            start_time = time(9,30,0),
            end_time = time(14,0,0),
            schedule = self.good_schedule
        )
    def test_instructors_cannot_contain_non_instructor(self): 
        users = ClassUser.objects.filter(id__in=[1,3,4])
  
        with self.assertRaisesMessage(ValidationError,"['Instructor cannot be a non Instructor user, the instructor value will be set to Null']"):
            Class.objects.create(
            name="Class two",
            owner=self.good_owner,
            description="The Best Class in the world ",
            start_date = self.good_start_date,
            end_date = self.good_end_date,
            start_time = time(9,30,0),
            end_time = time(14,0,0),
            schedule = self.good_schedule
        )
            class2 = Class.objects.get(id=2)
            
            class2.instructor.set(users)  
            class2.save() # save method needs to be invoked in every instructor update, otherwise we can't validate
    
    def test_bad_inputs_on_schedule(self): 
        with self.assertRaisesMessage(ValidationError,"['Please check the spelling of your days in a week, also be careful not to use whitespaces between commas']"): 
            Class.objects.create(
            name="Class two",
            owner=self.good_owner,
            description="The Best Class in the world ",
            start_date = self.good_start_date,
            end_date = self.good_end_date,
            start_time = time(9,30,0),
            end_time = time(14,0,0),
            schedule = "monday,tuesday,wednesday,thursday,friday,saturday, sunday"
        )
    
    def test_start_date_do_not_included_in_schedule(self): 
        with self.assertRaisesMessage(ValidationError,"['Your start date should be included into your schedule']"): 
            Class.objects.create(
            name="Class two",
            owner=self.good_owner,
            description="The Best Class in the world ",
            start_date = self.good_start_date,
            end_date = self.good_end_date,
            start_time = time(9,30,0),
            end_time = time(14,0,0),
            schedule = self.bad_schedule
        )
    def test_invalid_end_date_and_start_date_on_yesterday(self): 
        with self.assertRaisesMessage(ValidationError,"['You cannot set the end date < start date or start date < today']"): 
            Class.objects.create(
            name="Class two",
            owner=self.good_owner,
            description="The Best Class in the world ",
            start_date = self.good_start_date,
            end_date = self.bad_end_date,
            start_time = time(9,30,0),
            end_time = time(14,0,0),
            schedule = self.good_schedule
        )
        with self.assertRaisesMessage(ValidationError,"['You cannot set the end date < start date or start date < today']"): 
            Class.objects.create(
            name="Class two",
            owner=self.good_owner,
            description="The Best Class in the world ",
            start_date = self.bad_start_date,
            end_date = self.good_end_date,
            start_time = time(9,30,0),
            end_time = time(14,0,0),
            schedule = self.good_schedule
        )



    


   
        
        
        
