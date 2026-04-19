from gc import get_objects

from django.shortcuts import render, get_object_or_404
from .models import Post,Category, Tag

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
    comments = post.comments.all()
    context = {'post': post, 'comments': comments}
    context.update(get_category())
    return render(request,'blog/post.html', context)


def category(request, slug=None):
    c = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=c).order_by('-published_date')
    context = {'posts': posts}
    context.update(get_category())
    return render(request, 'blog/index.html', context)
