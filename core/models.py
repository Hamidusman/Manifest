from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blogpost(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length=10000)
   # category = models.

    def __str__(self):
        return self.title