from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from datetime import datetime, time
# Create your models here.
class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    about = models.CharField(max_length=60, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to='profile-pic/')
    email = models.EmailField(max_length= 50)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
 
 
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
    picture = models.FileField(upload_to='post-pic/')
    author = models.ForeignKey(User, related_name= 'posts', on_delete  = models.CASCADE)
    
    def __str__(self):
        return self.title

def save_post(sender, instance, **kwargs):
    print('Post created')

post_save.connect(save_post, sender=Post)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
    comment = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.post.author != self.user:
            Notification.objects.create(
                user = self.post.author,
                post = self.post, 
                message = f'{self.user.username} commented on {self.post.title}: {self.comment}'
            )
def save_comment(sender, instance, **kwargs):
    print('Comment Saved')
    def __str__(self):
        return self.comment

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications',  on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    message = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message