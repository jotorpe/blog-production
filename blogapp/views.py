from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from .models import Author, Category, Post, CategoryPersonal, PostPersonal

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    posts = Post.objects.order_by('-timestamp')[:3]
    # Render the HTML template index.html
    context = {
        'posts':posts,
    }
    return render(request,'index.html', context)
    
def about(request):
    return render(request, 'about.html')

def cv(request):
    return render(request, 'cv.html')

def post(request,slug):
    post = Post.objects.get(slug = slug)
    latest = Post.objects.order_by('-timestamp')[:3]
    # latest = Post.objects.order_by('-timestamp')[0]
    context = {
        'post': post,
        'latest': latest,
    }
    return render(request, 'post.html', context)

def post_all(request):
    posts = Post.objects.order_by('-timestamp')

    context = {
        'posts': posts,
    }
    return render(request, 'post_all.html', context)

@login_required
def postPersonal(request,slug):
    post = PostPersonal.objects.get(slug = slug)
    latest = PostPersonal.objects.order_by('-timestamp')[:3]
    # latest = Post.objects.order_by('-timestamp')[0]
    context = {
        'post': post,
        'latest': latest,
    }
    return render(request, 'postPersonal.html', context)

@login_required
def postPersonal_all(request):
    posts = PostPersonal.objects.order_by('-timestamp')

    context = {
        'posts': posts,
    }
    return render(request, 'postPersonal_all.html', context)

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        'searching_obj': queryset
    }
    return render(request, 'search_bar.html', context)

@login_required
def searchPersonal(request):
    queryset = PostPersonal.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        'searching_obj': queryset
    }
    return render(request, 'search_bar_personal.html', context)

def postcategories(request,slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_categories.html', context)