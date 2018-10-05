from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages

# Create your views here.
def index(request):
    post_list = Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')
    paginator = Paginator(post_list, 10)

    try:
        page = request.GET.get('page')
    except AttributeError:
        page = 1
    
    posts = paginator.get_page(page)

    context = {
        'title': 'Latest Entries',
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post, 
    }

    return render(request, 'posts/detail.html', context)

@login_required
def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.updated_at = timezone.now()
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Saved "{}"'.format(post.title))
            return redirect('details', id=post.id)

    else:
        form = PostForm()
        context = {
            'title': 'New Post',
            'form': form, 
        }

        return render(request, 'posts/edit.html', context)

@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.updated_at = timezone.now()
            post.save()
            messages.add_message(request, messages.INFO, 'Edited "{}"'.format(post.title))
            return redirect('details', id=post.id)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
    }
    return render(request, 'posts/edit.html', context)

@login_required
def post_draft_list(request):
    post_list = Post.objects.filter(published_at__isnull=True).order_by('created_at')
    paginator = Paginator(post_list, 10)

    try:
        page = request.GET.page('page')
    except AttributeError:
        page = 1
    posts = paginator.get_page(page)

    context = {
        'posts': posts,
        'title': 'Unpublished Posts'
    }

    return render(request, 'posts/index.html', context)

@login_required
def post_publish(request, id):
    post = get_object_or_404(Post, id=id)
    post.publish()
    messages.add_message(request, messages.SUCCESS, 'Published "{}"'.format(post.title))
    return redirect('index')

@login_required
def post_remove(request, id):
    post = get_object_or_404(Post, id=id)
    post_title = post.title
    post.delete()
    messages.add_message(request, messages.WARNING, 'Deleted "{}"'.format(post_title))
    return redirect('index')

def add_comment_to_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('details', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'posts/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.approve()
    return redirect('details', id=comment.post.id)

@login_required
def comment_remove(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect('details', id=comment.post.id)