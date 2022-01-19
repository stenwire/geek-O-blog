from django.shortcuts import render

posts = [
    {
        'author': 'Sten',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Dec, 12, 2056',
    },
    {
        'author': 'Chizoba',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Feb, 12, 2057',
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': about})