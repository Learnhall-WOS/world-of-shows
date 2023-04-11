from django.test import TestCase
from base.models import Show, Talent, Genre, Review, Theater
from django.contrib.auth.models import User
from random import randint
from datetime import datetime
from .helpers import Helper





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
    
    def test_custom_save_method(self): 
        show3 = Show.objects.create(
            name = "Amazing Show 3",
            host = self.theaters[0],
            description = "The third most amazing show",
        )
       
        show3.host_id = None # Test whether the logic of "if not self.host_id:    will reproduce host_id when called"
        show3.save()

        self.assertIsNotNone(show3.host_id)  #Test wether the save method will be able to reproduce host_id

class ReviewTestCase(TestCase): 
    """ unit testing for Review Model """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.helper = Helper()
        cls.user1 = User.objects.create(username="agus",password="agus123")
        cls.theater = Theater.objects.create(name="Theater 1", user=cls.user1)
        cls.show1 = Show.objects.create(
            name = "Amazing Show 1",
            host=cls.theater,
        )
        cls.seq_text = cls.helper.generate_sequential_string(100)

    def setUp(self):
        User.objects.create(username="Brian",password="BrianHandsome")
        Show.objects.create(
            name = "Amazing Show 2",
            host=self.theater,
        )
        Review.objects.create(
            author=self.user1,
            show=self.show1,
            text = self.seq_text
        )


    def test_object_string_repr(self): 
        """ test whether object is represented by truncated version of text field ( 50 characters ) """
        fifty_string = self.helper.generate_sequential_string(50)
        review1 = Review.objects.get(id=1)
        self.assertEqual(str(review1),fifty_string)
    

    
    



    

    
