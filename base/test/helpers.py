
from base.models import Show, Talent, Genre, Review, Theater
from django.contrib.auth.models import User
from random import randint

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