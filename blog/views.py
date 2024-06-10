from django.shortcuts import render, get_object_or_404, redirect
from . models import Blog, Tag
from django.contrib.auth import login as user_auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_auth_login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'authentications/login.html')
    else:
        return render(request, 'authentications/login.html')

def user_logout(request):
    logout(request)
    return redirect('home_page')

def home_page(request):
    blog = Blog.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home/home_page.html', {'blogs': blog, 'tags': tags})

# all blogs and with filters
def blogs(request):
    blogs = Blog.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home/blogs/all_blogs.html', {'blogs':blogs, 'tags': tags})

def delete_blog(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('blogs')

# blogs in reading mode
def blog_detail(request, id):
    blog_details = Blog.objects.get(pk=id)
    return render(request, 'home/blogs/blog_details.html', {'blog_details': blog_details})

@login_required
def user_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'home/blogs/user_blogs.html', {'blogs': blogs})


def add_blog(request):
    return render(request, 'home/blogs/new_blog.html')
