# Urls补充

## project(project/urls.py)中的urls.py常见的几种写法

1. 基于function的view
2. 基于class的view
3. view别名

## app中的urls.py的使用

在posts下新建一个urls.py文件

在project下的urls.py中设置第一级的路由
```
from django.conf.urls import url, include
from posts import urls as posts_urls
...
url(r'^post/', include(posts_urls)),
```
在app下的urls.py中设置第二级路由

```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.posts_home),
]
```

post_list
post_create
post_detail
post_update
post_delete

## 补充
1. 如果匹配到排在上面的正则表达式那么就不会适配下面的正则表达式了
2. 不要忘记加'^'和'$'