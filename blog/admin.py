from django.contrib import admin
from . models import Blog, Comments, CommentReplies, CommentLikes, BlogLikes, Categories


class blogAdmin(admin.ModelAdmin):
    list_display = ("title", 'author', 'created_at', 'category',)
admin.site.register(Blog, blogAdmin)

admin.site.register(Comments)
admin.site.register(CommentReplies)
admin.site.register(CommentLikes)
admin.site.register(BlogLikes)

class categoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
admin.site.register(Categories, categoriesAdmin)
