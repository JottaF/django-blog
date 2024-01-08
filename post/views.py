from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from post.forms import CreateComment, CreatePost
from .models import Comment, Post

def index(request):
    current_datetime = timezone.now()
    posts = Post.objects.all().filter(pub_date__lte=current_datetime).order_by('-pub_date', '-pk')
    return render(request, 'post/index.html', {'posts':posts})

def details(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CreateComment(request.POST)
            post = get_object_or_404(Post, pk=pk)
            
            if form.is_valid():
                Comment.objects.create(
                    user = request.user,
                    post = post,
                    content = form.cleaned_data['content']
                )
                return redirect('post:details', pk=pk)
            return render(request, 'post/invalidForm.html')
        return redirect('account_login')
    else:
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post/details.html', {'post':post})

def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreatePost(request.POST)

            if form.is_valid():
                new_post = Post.objects.create(
                    user = request.user,
                    title = form.cleaned_data['title'],
                    content = form.cleaned_data['content'],
                    pub_date = form.cleaned_data['pub_date'],
                    image = request.FILES.get('image')
                )
                
                return redirect('post:details', pk=new_post.pk)
            else:
                return redirect('post:create_post')
        else:
            current_date = timezone.now().strftime("%Y-%m-%d")
            return render(request, 'post/create_post.html', {'current_date':current_date})
    return redirect('account_login')

def remove_post(request, pk):
    user = request.user

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if user.is_authenticated:
            if user == post.user:
                post.delete()
                messages.success(request, 'Post apagado com sucesso!')
                return redirect('post:index')
            else:
                return redirect('post:not_allowed')
        else:
            return redirect('post:not_allowed')
    else:
        return render(request, 'post/remove_post.html', {'post':post})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user != post.user:
        return redirect('post:not_allowed')
    
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            
            return redirect('post:details', pk=post.pk)
        else:
            return redirect('post:edit_post')
    return render(request, 'post/edit_post.html', {'post': post})
        