from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from . import models
from . import forms
from django.urls import reverse


# Create your views here.

def posts_home(request):
    queryset = models.Post.objects.all()
    data = {
        "queryset": queryset,
        "name": "home",
        "age": "18",
    }
    return render(request, "base.html", data)
    # return redirect(reverse("detail", kwargs={"id": 3}))
    # return redirect("detail", 3)
    # return redirect("/post/3/")


def posts_detail(request, id=None):
    # obj = models.Post.objects.get(id=1)
    obj = get_object_or_404(models.Post, id=id)

    data = {
        "obj": obj
    }
    return render(request, "detail.html", data)


def posts_create(request):
    print(request.POST)  # 获取到提交的数据
    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # instance = models.Post.create(title=title, content=content)
    # instance.save()
    form = forms.PostForm(request.POST or None)
    if form.is_valid():  # 做数据有效性验证
        instance = form.save()  # 存数据库
    data = {
        "form": form
    }
    return render(request, "create.html", data)




def posts_update(request):
    return HttpResponse("<h1>posts_update</h1>")

def posts_delete(request):
    return HttpResponse("<h1>posts_delete</h1>")

class PostList(ListView):
    """post的视图类"""

    def get(self, request):
        return HttpResponse("<h1>post的视图类</h1>")
        