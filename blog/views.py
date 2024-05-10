from django.shortcuts import render
from . models import Blog

def home_page(request):
    blog = Blog.objects.all()
    return render(request, 'home/home_page.html', {'blogs': blog})
