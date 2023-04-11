from django.test import TestCase
from base.models import Show, Talent, Genre, Review, Theater
from django.contrib.auth.models import User
from random import randint
from datetime import datetime



""" I will only test the function or logic made by us, not by the framework. The test will be focused on 
overridden function, custom function, etc. I dont check properties of field or database, such as max_length, on_delete relationship, etc,  unless 
they are decided to become application mandatory spec. 
"""


# The helper class might be moved to different file in the future.

class Helper : 
    """ class to generate simple incremental data, generate random string, etc """

    def generate_simple_names(self,modelname,length): 
        return [f"{modelname} {x}" for x in range(length)]
    def generate_string(self,length): 
        """generate random string with specified length"""
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        for i in range(length+2): 
            result += chars[randint(0,len(chars)-1)] # generate random chars           
        return result 
    def generate_sequential_string(self,length): 
        result = ""
        increment = 0
        for i in range(1,length+1): 
            char = chr(65+increment)
            result += char
            if increment == 25 : 
                increment = 0 
            else : 
                increment += 1
        return result


    def generate_user_object(self,length): 
        user_names = self.generate_simple_names("user",length)
        result = []
        return ([User.objects.create(
                username=name,
                password=f"{name}123"
        )
        for name in user_names])
    def generate_genre_object(self,length): 
        genre_names = self.generate_simple_names("genre",length)
        return [Genre.objects.create(name=name) for name in genre_names]
    def generate_talent_object(self,length): 
        talent_names = self.generate_simple_names("talent",length)
        return [Talent.objects.create(name=name) for name in talent_names]
    def generate_theater_object(self,length): 
        theater_names = self.generate_simple_names("theater",length)
        user_objects = self.generate_user_object(length)
        return ([Theater.objects.create(
            name=name,
            user=user
        ) for name,user in zip(theater_names,user_objects)])



class TalentTestCase(TestCase): 
    """ Unit Testing for Talent Model """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Talent.objects.create(name="agus")    
   
    def test_talent_object_string_repr(self):
        """test whether the string representation of talent object is obtained from its name attribute"""
        talent = Talent.objects.get(id=1)
        self.assertEqual(str(talent),"agus")             

class GenreTestCase(TestCase): 
    """ Unit testing for Genre Model """
    @classmethod
    def setUpClass(cls): 
        super().setUpClass()
        Genre.objects.create(name="Comedy")
    
    def test_object_string_repr(self): 
        """test whether the string representation of genre object is obtained from its name attribute"""
        genre = Genre.objects.get(id=1)
        self.assertEqual(str(genre),"Comedy")

class TheaterTestCase(TestCase): 
    """ Unit Testing for Theater Model """
    @classmethod
    def setUpClass(cls): 
        super().setUpClass() 
        cls.user=User.objects.create(username="agus",password="agus123")
        cls.user2=User.objects.create(username="budi", password="budi123")
    
    def setUp(self): 
        Theater.objects.create(
            name = "Theater 1", 
            user = self.user
        )
        
        Theater.objects.create(
            name = "Theater 2",
            user = self.user2
        )
    
    def test_object_string_repr(self): 
        """test whether the string representation of genre object is obtained from its name attribute"""
        theater = Theater.objects.get(id=1)
        self.assertEqual(str(theater),"Theater 1")

class ShowTestCase(TestCase): 
    """ Unit testing for Show model """
    @classmethod
    def setUpClass(cls): 
        super().setUpClass()
        cls.helper = Helper()

    def setUp(self): 
        self.genres = self.helper.generate_genre_object(2) # generate 2 objects
        self.talents = self.helper.generate_talent_object(2)
        self.theaters = self.helper.generate_theater_object(2)
        self.show1 = Show.objects.create(
            name = "Amazing Show 1",
            host = self.theaters[0],
            description = "The only amazing show you'll ever need",
        )
        self.show1.genre.set(self.genres)
        self.show1.talent.set(self.talents)

        self.show2 = Show.objects.create(
            name="Amazing Show 2",
            host = self.theaters[1]
        )    
    def test_object_string_repr(self): 
        self.assertEqual(str(self.show1),"Amazing Show 1")

    def test_record_ordered_from_latest_updated(self): 
        show = Show.objects.all()
        first_appeared_record = show[0]
        self.assertEqual(str(first_appeared_record),"Amazing Show 2")
        show1 = Show.objects.get(id=1) 
        show1.name = "Amazing Show 1 updated" # updating the value of show1 to check whether the ordering change 
        show1.save()
        show = Show.objects.all()
        first_appeared_record = show[0]
        self.assertEqual(str(first_appeared_record),"Amazing Show 1 updated")
    
    # def test_custom_save_method(self): 
    #     show3 = Show.objects.create(
    #         name = "Amazing Show 3",
    #         host = self.theaters[0],
    #         description = "The third most amazing show",
    #     )
       
    #     show3.host_id = None # Test whether the logic of "if not self.host_id:    will reproduce host_id when called"
    #     show3.save()

    #     self.assertIsNotNone(show3.host_id)  #Test wether the save method will be able to reproduce host_id

class ReviewTestCase(TestCase): 
    """ unit testing for Review Model """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.helper = Helper()
        cls.user1 = User.objects.create(username="agus",password="agus123")
        cls.theater = Theater.objects.create(name="Theater 1", user=cls.user1)
        cls.author = User.objects.create(username="Steve", password="Steve123")
        cls.show1 = Show.objects.create(
            name = "Amazing Show 1",
            host=cls.theater,
        )

    def setUp(self):
        User.objects.create(username="Brian",password="BrianHandsome")
        Show.objects.create(
            name = "Amazing Show 2",
            host=self.theater,
        )
        Review.objects.create(
            author=self.user1,
            show=self.show1,
            text = "Review 1"
        )



    def test_object_string_repr(self): 
        """ test whether object is represented by truncated version of text field ( 50 characters ) """
        fifty_string = self.helper.generate_sequential_string(50)
        review1 = Review.objects.get(id=1)
        review1.text = self.helper.generate_sequential_string(100)
        self.assertEqual(str(review1),fifty_string)

    def test_record_ordered_from_latest_update(self): 
        review2 = Review.objects.create(
            author=self.author,
            show=self.show1, 
            text = "Review 2"
        )
        reviews = Review.objects.all()
        first_appeared_record = reviews[0]
      
        self.assertEqual(str(first_appeared_record),"Review 2")

        review1 = Review.objects.get(id=1)
        review1.text = "Review 1 updated"
        review1.save()
        reviews = Review.objects.all()

        first_appeared_record = reviews[0]
        self.assertEqual(str(first_appeared_record),"Review 1 updated")
    



    

    
