from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all().order_by("-date")[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
