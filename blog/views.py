from django.shortcuts import render, get_object_or_404
from . models import Blog, Categories

def home_page(request):
    blog = Blog.objects.all()
    
    return render(request, 'home/home_page.html', {'blogs': blog})


