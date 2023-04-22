from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from shows.models import Show, Genre, Talent, Theater, CastMember
from dataclasses import dataclass
from shows.forms import ShowForm

# class to save all global variables
@dataclass
class G:
    shows = Show.objects
    genres = Genre.objects
    users = User.objects
    theaters = Theater.objects
    talents = Talent.objects
    cast_members = CastMember.objects


# Create your views here.
def user_profile(request, pk):
    user = G.users.get(id=pk)
    cast_member = {}
    
    if hasattr(user, 'theater'):
        # get all shows associated with this user (as a theater)
        user_shows = G.shows.filter(host__user=user).distinct()
    elif hasattr(user, 'talent'):
        # all entries in the castmembers table associated with this talent
        cast_member_entries = G.cast_members.filter(talent__user=user)
        # print(cast_member_entries)
        # check if the user is a cast member
        if cast_member_entries.exists():
            cast_member['entries'] = cast_member_entries
            
            user_shows = G.shows.filter(cast__user=user).distinct()
        
    else:
        user_shows = []
    
    genres = G.genres.all()

    context = {'user': user, 'shows': user_shows,
               'genres': genres, 'cast_member': cast_member}

    return render(request, 'shows/profile.html', context)

def home_shows(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    shows = G.shows.filter(
        Q(genre__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__name__icontains=q)
        ).distinct()

    shows_count = shows.count()    
    genres = G.genres.all()
    context = {'shows': shows, 'genres': genres, 'shows_count': shows_count}
    return render(request, 'shows/home_shows.html', context)

def shows(request, pk):
    # pk: primary key
    show = G.shows.get(id=pk)
    cast = G.cast_members.filter(show=show)
    print(f'cast : {cast}')

    context = {'show': show, 'cast': cast}
    return render(request, 'shows/show.html', context)



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
    return render(request, 'shows/show_form.html', context)

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
    return render(request, 'shows/show_form.html', context)

@login_required(login_url='login')
def delete_show(request, pk):
    show = G.shows.get(id=pk)

    if request.user != show.host.user:
        return HttpResponse('You are not authorized to delete!')
    
    if request.method == 'POST':
        show.delete()
        return redirect('home')
    context = {'obj': show}
    return render(request, 'shows/delete.html', context)