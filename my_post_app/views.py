from django.shortcuts import render, redirect
from my_post_app.models import Post
from my_post_app.forms import PostForm
from django.shortcuts import get_object_or_404

def get_post(request):
    posts = Post.objects.all()
    return render(request, 'all_posts.html', locals())

def detail_post(request, pk):
    post = Post.objects.get(id=pk)
    # post = Post.objects.filter(id=pk)
    return render(request, 'detail_post.html', locals())

def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('post')

def create_post(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        print(name)
        description = request.POST.get("description")
        print(description)
        hashtag = request.POST.get("hashtag")
        print(hashtag)
        model = Post
        if name and description and hashtag:
            model.objects.create(name=name, description=description)
            return redirect('post')
    return render(request, 'create_post.html', locals())

def new_create(request):
    form = PostForm
    model = Post
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            model.objects.create(name=name, description=description)
            return redirect('post')
    return render(request, 'new_create.html', locals())
