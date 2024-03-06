from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=250)
    bio = models.CharField(max_length=250)
    image =  models.ImageField(upload_to='profile')
    
    
# Create your models here.
class BlogPosts(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=250)
    description =HTMLField()
    category = models.CharField(max_length=250)
    image =  models.ImageField(upload_to='posts') 
    created_at = models.DateTimeField(auto_now_add=True)


class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

