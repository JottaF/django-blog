from django.shortcuts import get_object_or_404, redirect, render

from post.forms import CreatePost
from .models import Comment, Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts':posts})

def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/details.html', {'post':post})

def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)

        if form.is_valid():
            new_post = Post.objects.create(
                user = request.user,
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                pub_date = form.cleaned_data['pub_date']
            )
            
            return redirect('post:details', pk=new_post.pk)
        else:
            return redirect('post:create_post')
    else:
        pass