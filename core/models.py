from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from datetime import datetime, time
# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    about = models.CharField(max_length=60)
    dob = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    phone = models.IntegerField(default= '0123')

    def __str__(self):
        return self.user.username

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
    
    def __str__(self):
        return self.title

def save_post(sender, instance, **kwargs):
    print('Post created')

post_save.connect(save_post, sender=Post)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

def save_comment(sender, instance, **kwargs):
    print('Comment Saved')
    def __str__(self):
        return self.comment

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.post.author != self.user:
            Notification.objects.create(
                user = self.post.author,
                post = self.post, 
                message = f'{self.user.username} commented on {self.post.title}'
            )

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    message = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message