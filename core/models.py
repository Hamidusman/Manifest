from django.db import models
from django.contrib.auth.models import User
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
    topic = models.CharField(choices = Topics, max_length=40)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.post.author != self.user:
            Notification.objects.create(
                user = self.post.author,
                post = self.post,
                message = f'{self.user.username} commente on {self.post.title}'
            )

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    message = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now=True)