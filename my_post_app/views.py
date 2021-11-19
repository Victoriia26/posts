from django.shortcuts import render
from my_post_app.models import Post

def get_post(request):
    posts = Post.objects.all()
    return render(request, 'all_posts.html', locals())

def detail_post(request, pk):
    post = Post.objects.get(id=pk)
    # post = Post.objects.filter(id=pk)
    return render(request, 'detail_post.html', locals())
