from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('blog-reading/<int:id>', views.blog_detail, name='blog_reading'),
    path('blogs', views.blogs, name="blogs"),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('delete-blog/<int:id>', views.delete_blog, name='delete_blog'),
    path('my-blogs', views.user_blogs, name="user_blogs"),
    path('add-blog', views.add_blog, name="new_blog"),
    path('update-blog/<int:blog_id>', views.update_blog, name="update_blog"),
    path('signup', views.registration, name='signup'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)