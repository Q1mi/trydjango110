from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.

def posts_home(request):
    return HttpResponse("<h1>Home</h1>")

def posts_create(request):
    return HttpResponse("<h1>posts_create</h1>")

def posts_detail(request):
    return HttpResponse("<h1>posts_detail</h1>")

def posts_update(request):
    return HttpResponse("<h1>posts_update</h1>")

def posts_delete(request):
    return HttpResponse("<h1>posts_delete</h1>")

class PostList(ListView):
    """post的视图类"""

    def get(self, request):
        return HttpResponse("<h1>post的视图类</h1>")
        