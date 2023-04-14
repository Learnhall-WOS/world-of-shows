from django.shortcuts import render
from classes.models import Class,ClassUser
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    classes = Class.objects.all()
    paginator = Paginator(classes,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'classes':classes,
        'page_obj':page_obj
    }

    return render(request,'classes/home.html',context)