from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

from datetime import datetime
# Create your views here.
def index(request):
    
    posts = Post.objects.all()[:10]

    context = {
        'title': 'Latest Entries',
        'posts': posts
    }

    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post, 
    }

    return render(request, 'posts/detail.html', context)

def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = datetime.now()
            post.save()

            return redirect('details', id=post.id)

    else:
        form = PostForm()
        context = {
            'title': 'New Post',
            'form': form, 
        }

        return render(request, 'posts/post_edit.html', context)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = requst.user
            post.created_at = datetime.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
    }
    return render(request, 'posts/post_edit.html', context)


