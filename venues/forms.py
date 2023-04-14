from django.contrib.auth.models import User
from django import forms
from .models import Venues, GeneralLocation, RequestRent



class FilteringForm(forms.ModelForm):
    status_list = [('', '----------'), ('F', 'Free'),('P', 'Paid'),]
    Choices = GeneralLocation.objects.all().values_list('name', 'name')         #to automatically add every created city into the filtering location forms
    choice_list= []
    for item in Choices:
        choice_list.append(item)
    location = forms.CharField(label='location', widget=forms.Select(
                       choices= choice_list)
    )
    start_date = forms.DateField(label='start_date', widget=forms.DateInput(
                       attrs={'PlaceHolder':'yyy-mm-dd'},)              
    )
    end_date = forms.DateField(label='end_date', widget=forms.DateInput(
                       attrs={'PlaceHolder':'yyy-mm-dd'},)              
    )   
    
    status = forms.CharField(label='status', widget=forms.Select(
                       choices= status_list )
    )
    class Meta:
        model = Venues
        fields = ['location','start_date','end_date','status',]


class CreatVenueForm(forms.ModelForm):
    class Meta:
        '''
            metadata
        '''
        model = Venues
        fields = '__all__'





class RequestRentForm(forms.ModelForm):
    name = forms.CharField(label = 'Name', widget=forms.TextInput(
                attrs={'PlaceHolder': "John Doe"}
            )
    )
    email=forms.EmailField(label = 'Email', widget= forms.EmailInput(
                attrs:={'PlaceHolder': "Work email"}
            )
    )
    start_date= forms.DateField(label= 'Start', widget=forms.DateInput(
            attrs:={'PlaceHolder': "yyy-mm-dd"}
            )
    )
    end_date= forms.DateField(label= 'End', widget=forms.DateInput(
            attrs:={'PlaceHolder': "yyy-mm-dd"}
            )
    )

    class Meta:
        model = RequestRent
        fields = ['name','email','start_date','end_date',]

    
    