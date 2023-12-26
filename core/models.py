from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    about = models.CharField(max_length=60)
    dob = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    phone = models.IntegerField(default= '0123')

    def __str__(self):
        return self.user
category = [
            ('Web Development', 'Web Development'),
            ('AI/ML', 'AI/ML'),
            ('UI/UX', 'UI/UX'),
            ('Programming', 'Programming'),
            ('Cyber Security', 'Cyber Security')
            ]

class Post(models.Model):
    title = models.CharField(max_length=30)
    read = models.CharField(max_length=100000)
    category = models.CharField(choices = category, max_length=40)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
