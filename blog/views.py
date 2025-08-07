from django.shortcuts import render
from .models import Post

def blog_home(request):
    posts = Post.objects.all().order_by('-date')  # Use 'date', not 'date_posted'
    return render(request, 'blog/home.html', {'posts': posts})
