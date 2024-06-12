from django.shortcuts import render, get_object_or_404, redirect
from . models import Blog, Tag
from django.contrib.auth import login as user_auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
@login_required
def delete_blog(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('blogs')

# blogs in reading mode
def blog_detail(request, id):
    blog_details = Blog.objects.get(pk=id)
    return render(request, 'home/blogs/blog_details.html', {'blog_details': blog_details})

@login_required
# user blogs
def user_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'home/blogs/user_blogs.html', {'blogs': blogs})

# add blog
@login_required
def add_blog(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST['title']
            description = request.POST['description']
            content = request.POST['content']
            thumbnail = request.FILES['thumbnail']
            tags = request.POST.getlist('tags')
            
            # create blog
            blog = Blog.objects.create(
                title=title,
                description=description,
                content=content,
                thumbnail=thumbnail,
                author=request.user,
            )
            # save tag
            blog.tags.set(tags)
            return redirect('home_page')

    tags = Tag.objects.all()
    return render(request, 'home/blogs/new_blog.html', {'tags': tags})


@login_required
def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        if request.user.is_authenticated and request.user == blog.author:
            title = request.POST['title']
            description = request.POST['description']
            content = request.POST['content']
            tags = request.POST.getlist('tags')

            blog.title = title
            blog.description = description
            blog.content = content
            
            if 'thumbnail' in request.FILES:
                blog.thumbnail = request.FILES['thumbnail']

            blog.tags.set(tags)
            blog.save()
            return redirect('home_page')
    
    tags = Tag.objects.all()
    return render(request, 'home/blogs/update_blog.html', {'blog': blog, 'tags': tags})
