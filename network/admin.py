from django.contrib import admin

from .models import User, Post, UserUser, UserPost

# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(UserUser)
admin.site.register(UserPost)
