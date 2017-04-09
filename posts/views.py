from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from . import models
from . import forms
from django.urls import reverse
from django.contrib import messages


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
        messages.add_message(request, messages.INFO, "帖子创建成功啦！")
        return redirect(instance.get_absolute_url())
    data = {
        "form": form
    }
    return render(request, "create.html", data)


def posts_update(request, id=None):
    """
    修改帖子的视图
    """
    obj = get_object_or_404(models.Post, id=id)
    form = forms.PostForm(request.POST or None, instance=obj)
    if form.is_valid():  # 做数据有效性验证
        instance = form.save()  # 存数据库
        messages.add_message(request, messages.INFO, "帖子更新成功啦！")
        return redirect(instance.get_absolute_url())
    data = {
        "form": form
    }
    return render(request, "create.html", data)




def posts_delete(request, id=None):
    obj = get_object_or_404(models.Post, id=id)  # 查找帖子，获取帖子对象
    obj.delete()  # 删除帖子
    return redirect("post:list")  # 使用url的命名空间进行跳转
    # return redirect("/post/")  # 跳转到 ip:port/**/，此处使用的是具体的url





class PostList(ListView):
    """post的视图类"""

    def get(self, request):
        return HttpResponse("<h1>post的视图类</h1>")
        