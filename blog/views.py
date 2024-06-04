from django.shortcuts import render, get_object_or_404
from . models import Blog, Tag

def home_page(request):
    blog = Blog.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home/home_page.html', {'blogs': blog, 'tags': tags})

# all blogs and with filters
def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'home/blogs/all_blogs.html', {'blogs':blogs})

# blogs in reading mode
def blog_detail(request, id):
    blog_details = Blog.objects.get(pk=id)
    return render(request, 'home/blogs/blog_details.html', {'blog_details': blog_details})



