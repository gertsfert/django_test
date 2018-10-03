from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def index(request):

    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')

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
            post.created_at = timezone.now()
            post.save()

            return redirect('details', id=post.id)

    else:
        form = PostForm()
        context = {
            'title': 'New Post',
            'form': form, 
        }

        return render(request, 'posts/edit.html', context)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('details', id=post.id)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
    }
    return render(request, 'posts/edit.html', context)

def post_draft_list(request):
    posts = Post.objects.filter(published_at__isnull=True).order_by('created_at')

    context = {
        'posts': posts,
        'title': 'Unpublished Posts'
    }

    return render(request, 'posts/index.html', context)

def post_publish(request, id):
    post = get_object_or_404(Post, id=id)
    post.publish()
    return redirect('details', id=post.id)
