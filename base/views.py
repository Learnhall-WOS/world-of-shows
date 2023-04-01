from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 

from .models import Show, Genre
from dataclasses import dataclass
from .forms import ShowForm

# class to save all global variables
@dataclass
class G:
    shows = Show.objects
    genres = Genre.objects

# Create your views here.

def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password does not match the username')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           user.save()
           login(request, user)
           return redirect('home')
       else:
           messages.error(request, 'An error occurred during registration.')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    shows = G.shows.filter(
        Q(genre__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    shows_count = shows.count()    
    genres = G.genres.all()
    context = {'shows': shows, 'genres': genres, 'shows_count': shows_count}
    return render(request, 'base/home.html', context)

def shows(request, pk):
    # pk: primary key
    show = G.shows.get(id=pk)
    context = {'show' : show}
    return render(request, 'base/show.html', context)

@login_required(login_url='login')
def post_show(request):
    form = ShowForm()
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/show_form.html', context)

@login_required(login_url='login')
def update_show(request, pk):
    show = G.shows.get(id=pk)
    form = ShowForm(instance=show)

    if request.user != show.host:
        return HttpResponse('You are not authorized to update!')

    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/show_form.html', context)

@login_required(login_url='login')
def delete_show(request, pk):
    show = G.shows.get(id=pk)

    if request.user != show.host:
        return HttpResponse('You are not authorized to delete!')
    
    if request.method == 'POST':
        show.delete()
        return redirect('home')
    context = {'obj': show}
    return render(request, 'base/delete.html', context)