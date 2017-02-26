from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from . import models

# Create your views here.

def posts_home(request):
    queryset = models.Post.objects.all()
    data = {
        "queryset": queryset,
        "name": "home",
        "age": "18",
    }
    return render(request, "base.html", data)

def posts_create(request):
    data = {
        "name": "create",
        "age": "28",
    }
    return render(request, "index.html", data)

def posts_detail(request):
    # obj = models.Post.objects.get(id=1)
    obj = get_object_or_404(models.Post, id=3)

    data = {
        "obj": obj
    }
    return render(request, "detail.html", data)

def posts_update(request):
    return HttpResponse("<h1>posts_update</h1>")

def posts_delete(request):
    return HttpResponse("<h1>posts_delete</h1>")

class PostList(ListView):
    """post的视图类"""

    def get(self, request):
        return HttpResponse("<h1>post的视图类</h1>")
        