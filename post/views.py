from django.shortcuts import get_object_or_404, render
from .models import Comment, Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts':posts})

def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/details.html', {'post':post})