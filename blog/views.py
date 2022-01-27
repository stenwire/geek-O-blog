from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Sten',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 12, 2056',
    },
    {
        'author': 'Chizoba',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 12, 2057',
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
