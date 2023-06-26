from django.contrib import admin

# Register your models here.

from .models import Author, Category, Post, CategoryPersonal, PostPersonal

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(CategoryPersonal)
admin.site.register(PostPersonal)