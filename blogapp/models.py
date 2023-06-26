from django.db import models
from django.contrib.auth import get_user_model # helper function to fetch the User model for the project
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

User = get_user_model()

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True) # is similar to a ForeignKey with unique=True
    bio = models.TextField()
    profile_picture = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ["user","bio"]

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField() # short label generally used in URLs, nicer look for users

    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category,blank=True)
    featured = models.BooleanField(blank=True, null=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.title
    

class CategoryPersonal(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField() # short label generally used in URLs, nicer look for users

    def __str__(self):
        return self.title

class PostPersonal(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(CategoryPersonal,blank=True)
    featured = models.BooleanField(blank=True, null=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.title