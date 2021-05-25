from django.shortcuts import render

from .models import Post, Category, Tag

def index(request):
    context = {
        'posts': Post.objects.all().order_by('-created_at'),
        'categories': Category.objects.all(),
        'tags': Tag.objects.all()
    }
    return render(request, 'blog/index.html', context=context)


def details(request, pk=None):
    context = {
        'post': Post.objects.get(pk=pk) if pk is not None else None
    }
    return render(request, 'blog/post.html', context=context)


def create(request):
    context = {}
    return render(request, 'blog/create.html', context=context)
