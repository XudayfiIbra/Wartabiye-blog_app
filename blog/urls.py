from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('blog-reading/<int:id>', views.blog_detail, name='blog_reading'),
    path('blogs', views.blogs, name="blogs"),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)