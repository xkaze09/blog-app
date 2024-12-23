from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Christian Salinas',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 23, 2024'
    },
    {
        'author': 'Christian Salinas',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 24, 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})