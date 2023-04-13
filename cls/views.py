from django.shortcuts import render
from cls.models import User,ClassUser

# Create your views here.
def home(request): 
    return render(request,'cls/home.html')