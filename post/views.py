from django.shortcuts import get_object_or_404, redirect, render

from post.forms import CreateComment, CreatePost
from .models import Comment, Post

def index(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'post/index.html', {'posts':posts})

def details(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CreateComment(request.POST)
            print(form)
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
        
        return render(request, 'post/create_post.html', {})
    return redirect('account_login')
    