from django.shortcuts import render
from classes.models import Class,ClassUser
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    q=request.GET.get("q")
    if not q or q == "None" or q=="" :
        classes = Class.objects.all()
    else : 
        classes = Class.objects.filter(
            Q(name__icontains=q) |
            Q(owner__user__username__icontains=q) |
            Q(description__icontains=q) |
            Q(schedule__icontains=q) |
            Q(instructor__user__username__icontains=q)
         ).distinct()
    paginator = Paginator(classes,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'query':q,
        'classes':classes,
        'page_obj':page_obj
    }
    return render(request,'classes/home.html',context)