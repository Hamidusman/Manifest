from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    about = models.CharField(max_length=60)
    dob = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    phone = models.IntegerField(default=)

    def __str__(self):
        return self.user
category = [
            ('Web Development', 'Web Development'),
            ('AI/ML', 'AI/ML'),
            ('UI/UX', 'UI/UX'),
            ('Programming', 'Programming'),
            ('Cyber Security', 'Cyber Security')
            ]
class Blogpost(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length=100000)
    category = models.CharField(choices=category, default='Programming', max_length=30)

    def __str__(self):
        return self.title