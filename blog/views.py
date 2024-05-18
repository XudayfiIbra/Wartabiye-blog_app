from django.shortcuts import render, get_object_or_404
from . models import Blog, Tag

def home_page(request):
    blog = Blog.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home/home_page.html', {'blogs': blog, 'tags': tags})


