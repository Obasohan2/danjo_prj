from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Community
from django.contrib.auth.decorators import login_required


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        Comment.objects.create(
            post=post,
            author=request.user,
            text=request.POST['comment']
        )
        return redirect('post_detail', pk=pk)
    return render(request, 'core/post_detail.html', {'post': post})

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', pk=pk)


def community_view(request, community_name):
    community = get_object_or_404(Community, name=community_name)
    posts = Post.objects.filter(community=community).order_by('-created_at')
    return render(request, 'core/community.html', {'posts': posts, 'community': community})
