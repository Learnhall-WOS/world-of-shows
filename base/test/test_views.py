from django.test import TestCase
from django.test import Client
from django.urls import reverse
from base.views import RoleChoiceForm
from django.contrib.messages import get_messages
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from base.models import Talent,Theater


class TestRegisterPage(TestCase): 
    def setUp(self): 
        self.postdata = {
            "username":"agus",
            "password1":"agustinus123",
            "password2":"agustinus123",
            "role":"T"
        }

        User.objects.create(username="budi",password="budi123456") # Create existing user during the test

        self.register_url = reverse("register")
        self.home_url = reverse("home")

    def test_post_good_data_status_code(self): 
        url = reverse("login")
        response = self.client.post(self.register_url,self.postdata, follow=True)
        self.assertEqual(response.status_code,200)
     

    def test_post_bad_data_password_not_match_status_code(self):
        """test whether the error messages appeared when password1 and password2 do not match"""
        #setup data
        bad_data = self.postdata
        bad_data["password2"] = "notmatchedpassword123"
        response = self.client.post(self.register_url,bad_data, follow=True)
      
        messages = list(get_messages(response.wsgi_request))[0]
     
        #test
        self.assertEqual(str(messages),"An error occurred during registration.")

    def test_post_data_bad_username_and_password_inputs(self): 
        """ Test whether the error mesages are delivered to the user when application is given bad inputs """
        #setup data
        bad_username = self.postdata.copy()
        bad_username["username"] = "agus:#4578"
        response_bad_username = self.client.post(self.register_url,bad_username,follow=True)
        message_bad_username = list(get_messages(response_bad_username.wsgi_request))[0]
        bad_password = self.postdata.copy()
        bad_password["password1"] = "one"
        bad_password["password2"] = "one"
        response_bad_password = self.client.post(self.register_url,bad_password,follow=True)
        message_bad_password = list(get_messages(response_bad_password.wsgi_request))[0]
        err_str = str(response_bad_password.context["fields"][2])
        bs = BeautifulSoup(err_str,"html.parser")
        pw_too_sort_error_msg = bs.find("li").text

        #test
        self.assertEqual(str(message_bad_username),"An error occurred during registration.")
        self.assertFormError(response_bad_username,"form","username","Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.")
        self.assertEqual(str(message_bad_password),"An error occurred during registration.")
        self.assertEqual(pw_too_sort_error_msg,"This password is too short. It must contain at least 8 characters.")

    def test_post_data_user_already_exist(self): 
        """ Test whether the error messages are delivered when user try to use existing user """
        #setup data 
        user = User.objects.get(id=1)
        existing_user = {
            "username":user.username,
            "password1":user.password,
            "password2":user.password,
            "role":"T"
        }
        
        response = self.client.post(self.register_url,existing_user)
        bs = BeautifulSoup(response.content,'html.parser')
        error_msg = bs.select_one("ul.errorlist li").text

        #test
        self.assertEqual(error_msg,"A user with that username already exists.")
    
    def test_username_lowercased(self): 
        """ Test whether the username is stored as lower case version of the inputs """
        #setup_data
        upper_case_name = self.postdata
        upper_case_name["username"] = "JOHN_HANDSOME"
        response = self.client.post(self.register_url,upper_case_name,follow=True)
        user = User.objects.get(id=2)

        #test 
        self.assertEqual(str(user),"john_handsome")
    
    def test_creation_of_talent_and_theater_object(self): 

        #setup_data
        theater_data = self.postdata.copy() #use default username declared in setUp method 
        talent_data = self.postdata.copy()
        talent_data["username"] = "Peter"
        talent_data["role"] = "A"
        self.client.post(self.register_url,theater_data,follow=True)
        self.client.post(self.register_url,talent_data,follow=True)



        talent_object = Talent.objects.get(id=1)
        theater_object = Theater.objects.get(id=1)

        #test 
        self.assertEqual(str(talent_object),"peter")
        self.assertEqual(str(theater_object),"agus")
    
    def test_redirected_page_after_register(self): 
        #setup_data 
        response = self.client.post(self.register_url,self.postdata)   
             
        #test 
        self.assertAlmostEqual(response.status_code, 302)
        self.assertEqual(response.url,self.home_url)






        