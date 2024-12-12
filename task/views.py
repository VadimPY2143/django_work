from django.shortcuts import render, redirect
from forms import CreatePost
from models import Post


def create_post(request):
    if request.method == 'POST':
        form = CreatePost()
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CreatePost()

    return render(request, 'create_post.html', {'form': form})


def post_list_view(request):
    post = Post.objects.all().order_by('-date')
    return render(request, 'post_list.html', {'post': post})







