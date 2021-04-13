from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField


class User(AbstractUser):
    pass

class Post(models.Model):
    content = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} said: {self.content} @ {self.created}'.format(self=self)

class UserUser(models.Model):
    following = models.ManyToManyField(User, related_name="followers")

    def __str__(self):
        return f'{self.following}'.format(self=self)

class UserPost(models.Model):
    user = models.ManyToManyField(User, related_name="user")
    post = models.ManyToManyField(Post, related_name="post")

    def __str__(self):
        return f'{self.user} posted {self.post}'.format(self=self)