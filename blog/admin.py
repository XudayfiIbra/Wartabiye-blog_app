from django.contrib import admin
from . models import Blog, Comments, CommentReplies, CommentLikes, BlogLikes, Categories

admin.site.register(Blog)
admin.site.register(Comments)
admin.site.register(CommentReplies)
admin.site.register(CommentLikes)
admin.site.register(BlogLikes)
admin.site.register(Categories)
