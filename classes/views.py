from django.shortcuts import render,get_object_or_404
from classes.models import Class,ClassUser
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request):
    q=request.GET.get("q")
    if not q or q=="" or q=="None" :
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

def detail(request,pk):
    class_detail = get_object_or_404(Class,pk=pk)
    context = {
        'class':class_detail
    }
    return render(request,'classes/detail.html',context)