from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=400)
    #test= models.CharField(max_length=223, null=True)
    content = models.TextField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='uploaded_images')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class BlogLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} likes {self.blog.title}"
    
    @staticmethod
    def total_likes(blog_id):
        return BlogLikes.objects.filter(blog_id=blog_id).aggregate(total_likes=Count('id'))['total_likes'] 

class Comments(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username} comments {self.blog.title}"


class CommentLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} likes {self.comment}"


class CommentReplies(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Parent_comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username} replies {self.Parent_comment}"
    
    
    

    