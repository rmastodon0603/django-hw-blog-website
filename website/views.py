from django.shortcuts import render

from django.shortcuts import redirect

from .models import Post, Category, Tag

from .forms import PostForm

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
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published = True
            post.save()
            form.save_m2m()
        return redirect('index')

    form = PostForm()


    return render(request, 'blog/create.html', {'form': form})
