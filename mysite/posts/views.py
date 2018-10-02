from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
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
    form = PostForm()

    context = {
        'form': form, 
    }

    return render(request, 'posts/post_edit.html', context)
