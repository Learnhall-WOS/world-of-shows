from dataclasses import dataclass
from datetime import datetime, date


from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from .models import Venues, GeneralLocation, RequestRent
from .forms import FilteringForm,CreatVenueForm, RequestRentForm
# Create your views here.


@dataclass
class G:
	ven = Venues.objects
	


def venue_home(request):
    ven = G.ven.all() 
    venue_count = ven.count()
    form = FilteringForm(request.POST or None)
    
    if request.method == 'POST':
         
        try:
            #filtering from venues
            ven = G.ven.filter(
                general__name__icontains= form['location'].value(),
                start_date__range= [ form['start_date'].value(),
                                    form['end_date'].value()
                                    ],
                status__icontains= form['status'].value(),
            )
        except:
            ven = ven

    return render(request, 'venues/venue.html', {'ven': ven,'venue_count':venue_count,'form':form,})



def details(request, slug):
    detail = G.ven.get(slug=slug)

    rent = RequestRentForm(instance= detail)
    if request.method == 'POST':
        rent = RequestRentForm(request.POST, instance=detail))
        if rent.is_valid(): 
            rent.save(commit=False)
            c= RequestRent(venue =G.ven.get(slug=slug), 
                    name=rent.cleaned_data['name'], 
                    email=rent.cleaned_data['email'], start_date=rent.cleaned_data['start_date'], 
                    end_date=rent.cleaned_data['end_date'],
                    created=datetime.now() 
            )
            c.save()
            return redirect('detail', detail.slug )
    else:
        rent= RequestRentForm()

    return render(request, 'venues/detail.html', {'detail': detail, 'rent': rent,})


@login_required(login_url='login')
def createvenue(request):
    form = CreatVenueForm()
    if request.method == 'POST':
        form = CreatVenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venue')
    
    return render(request, 'venues/venue_post.html', {'form': form})


@login_required(login_url='login')
def venue_edit(request, id):
    edit = G.ven.get(pk=id)
    form = CreatVenueForm(instance=edit)
    if request.method == 'POST':
        form = CreatVenueForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('venue', edit.pk)
        else:
            form = CreatVenueForm(instance= edit)
    
    return render(request, 'venues/venue_post.html', {'form': form})

def remove_venue(request):
    deletevenue = request.POST['deletevenue']
    Venues.objects.filter(pk=deletevenue).delete()
    return redirect('venue')


