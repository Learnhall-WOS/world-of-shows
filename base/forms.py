from django.forms import ModelForm
from .models import Show

class ShowForm(ModelForm):
    class Meta:
        '''
            metadata
        '''
        model = Show
        fields = '__all__'