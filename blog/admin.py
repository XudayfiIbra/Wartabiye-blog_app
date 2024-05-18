from django.contrib import admin
from . models import Blog, Comments, CommentReplies, CommentLikes, BlogLikes, Tag




class blogAdmin(admin.ModelAdmin):
    list_display = ("title", 'author', 'created_at',)
    list_filter = ('tags',)
    search_fields = ('title', 'author',)
admin.site.register(Blog, blogAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Comments)
admin.site.register(CommentReplies)
admin.site.register(CommentLikes)
admin.site.register(BlogLikes)
admin.site.register(Tag)

