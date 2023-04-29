from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import models
from .models import Play

def home_play_reads(request):
    # Retrieve all plays from the database
    plays = Play.objects.all()

    # Check if the user submitted a search query
    query = request.GET.get('q')
    if query:
        # Filter the plays based on the search query
        plays = plays.filter(
            models.Q(name__icontains=query) |
            models.Q(author__icontains=query) |
            models.Q(genre__icontains=query)
        )

    # Render the template with the list of plays and the search bar
    return render(request, 'playreads/home_play_reads.html', {
        'plays': plays,
        'query': query,
    })

def play_detail(request, play_id):
    # Retrieve the play from the database
    play = get_object_or_404(Play, pk=play_id) # play = Play.objects.get(pk=play_id)

    # Render the template with the play details and the participation form
    return render(request, 'playreads/play_detail.html', {
        'play': play,
    })

def participate(request, play_id):
    # Retrieve the play from the database
    play = get_object_or_404(Play, pk=play_id) # play = Play.objects.get(pk=play_id)

    if request.method == 'POST':
        # Process the form submission ToDo: add data validation / cleaning
        name = request.POST['name']
        email = request.POST['email']

        # Send an email to the organizer(s) of the play read (Optional)
        # ...

        # Display a success message to the user
        messages.success(request, f'Thank you for signing up for the {play.name} play read!')
        return redirect('play_detail', play_id=play.pk)

    # If the form submission failed, or if the user accessed this URL directly,
    # render the play detail template with an error message
    messages.error(request, 'There was an error processing your request. Please try again.')
    return redirect('play_detail', play_id=play.pk)