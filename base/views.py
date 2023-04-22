from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from base.forms import RoleChoiceForm
from shows.models import Talent, Theater

# Create your views here.
def home(requset):
    return render(requset, 'home.html')


def register_page(request):
    form = RoleChoiceForm()
    if request.method == 'POST':
       form = RoleChoiceForm(request.POST)
       if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           # Save the user object before using it to create related object
           user.save() 
           # create a theater or talent object based on user's role
           if form.cleaned_data['role'] == 'T':
               Theater.objects.create(user=user, name=user.username)
           elif form.cleaned_data['role'] == 'A':
               Talent.objects.create(user=user, name=user.username)

           login(request, user)
           return redirect('home')
       else:
           messages.error(request, 'An error occurred during registration.')

    context = {'form': form}
    return render(request, 'shows/login_register.html', context)

def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        try:
            user = User.objects.get(username=username)
            
        except:
            messages.error(request, 'User does not exist')
            print("User does not exist")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password does not match the username')
            print("Password does not match the username")

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

    



