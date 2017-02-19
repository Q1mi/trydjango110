# 我们的第一个view（视图）

posts/views.py

定义了我们第一个视图

```
from django.http import HttpResponse

def posts_home(request):
    return HttpResponse("Hello world!")
```

## url建立映射到view
bbs/urls.py
```
from posts import views

加一行：
url(r'^home/', views.posts_home),
```