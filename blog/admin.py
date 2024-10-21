from django.contrib import admin

from .models import Blogger, BlogPost, Comment

# Register your models here.
admin.site.register(Blogger)
admin.site.register(BlogPost)
admin.site.register(Comment)
