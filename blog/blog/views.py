from gc import get_objects


from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import title
from django.db.models import Q
from .models import Post, Category, Tag, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages


def func1():
    return "hello world"

def get_category():
    all = Category.objects.all()
    count = all.count()
    return {'cat1': all[:count // 2], 'cat2': all[count // 2:]}

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-published_date')
    context = {'posts': posts}
    context.update(get_category())
    return render(request,'blog/index.html', context)


def about(request):
    context = {}
    context.update(get_category())
    return render(request,'blog/about.html', context)


def post(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-published_date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.published_date = now()
            new_comment.save()
            form.save_m2m()
            messages.success(request, 'Comment created successfully')
            return redirect('post', slug=post.slug)
    else:
        form = CommentForm()
    context = {'post': post, 'comments': comments, "form": form}
    context.update(get_category())
    return render(request,'blog/post.html', context)


def category(request, slug=None):
    c = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=c).order_by('-published_date')
    context = {'posts': posts}
    context.update(get_category())
    return render(request, 'blog/index.html', context)

def tag(request, slug=None):
    t = get_object_or_404(Tag, slug=slug)
    posts_list = Post.objects.filter(tags=t).order_by('-published_date')
    context = {'posts': posts_list, 'tag': t}
    context.update(get_category())
    return render(request, 'blog/index.html', context)

def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query)).order_by('-published_date')
    context = {'posts': posts}
    context.update(get_category())
    return render(request,'blog/index.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.published_date = now()
            new_post.user = request.user
            new_post.save()
            form.save_m2m()
            messages.success(request, 'Post created successfully')
            return redirect('index')
    else:
        form = PostForm()
    context = {'form': form}
    context.update(get_category())
    return render(request, 'blog/create_post.html', context)
