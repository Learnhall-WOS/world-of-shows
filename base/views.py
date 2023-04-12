from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from .models import Show, Genre, Talent, Theater
from dataclasses import dataclass
from .forms import ShowForm, RoleChoiceForm

# class to save all global variables
@dataclass
class G:
    shows = Show.objects
    genres = Genre.objects
    users = User.objects
    theaters = Theater.objects
    talents = Talent.objects


# Create your views here.

def register_page(request):
    form = RoleChoiceForm()
    if request.method == 'POST':
       form = RoleChoiceForm(request.POST)
       if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           user.save()
           # create a theater or talent object based on user's role
           if form.cleaned_data['role'] == 'T':
               Theater.objects.create(user=user, name=user.username)
           elif form.cleaned_data['role'] == 'A':
               Talent.objects.create(name=user.username)

           login(request, user)
           return redirect('home')
       else:
           messages.error(request, 'An error occurred during registration.')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)

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

    
def user_profile(request, pk):
    theater = G.users.get(id=pk)
    
    # print(f'user: {user}')
    theater_shows = G.shows.filter(host__user=theater) # all shows associated with this user
    genres = G.genres.all()

    context = {'user': theater, 'shows': theater_shows,
               'genres': genres}

    return render(request, 'base/profile.html', context)

    

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    shows = G.shows.filter(
        Q(genre__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        ).distinct()

    shows_count = shows.count()    
    genres = G.genres.all()
    context = {'shows': shows, 'genres': genres, 'shows_count': shows_count}
    return render(request, 'base/home_shows.html', context)

def shows(request, pk):
    # pk: primary key
    show = G.shows.get(id=pk)
    cast = show.talent.all()

    context = {'show': show, 'cast': cast}
    return render(request, 'base/show.html', context)



@login_required(login_url='login')
def post_show(request):
    # Check if the current user is associated with a theater
    if not hasattr(request.user, 'theater'):
        messages.error(request, 'Only theaters can post shows.')
        return redirect('home')
    
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

    if request.user != show.host.user:
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

    if request.user != show.host.user:
        return HttpResponse('You are not authorized to delete!')
    
    if request.method == 'POST':
        show.delete()
        return redirect('home')
    context = {'obj': show}
    return render(request, 'base/delete.html', context)