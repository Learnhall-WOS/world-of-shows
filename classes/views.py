from django.shortcuts import render
from classes.models import User,ClassUser

# Create your views here.
def home(request): 
    return render(request,'classes/home.html')