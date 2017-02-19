# No.6 定制admin

## 上个视频的补充

posts/models.py中class Post下面的__str__(self)的作用

## 本节内容

在post/admin.py文件中添加如下代码：

```
class PostAdmin(admin.ModelAdmin):

    list_display = [,]  # 控制页面展示哪些字段
    list_display_links = [,]  # 控制哪些字段是超链接
    list_filter = [,]  # 支持在右侧过滤的字段
    search_fields = [,]  # 支持搜索的字段
    list_editable = [,]  # 支持直接编辑的字段，注意！不能与list_display_links重复！

    class Meta:
        model = model.Post

```

## 补充
如何修改admin中显示的app名字？

1. 在posts/apps.py中
PostsConfig类中添加
verbose_name = "帖子"

2. posts/__init__.py

```
default_app_config = "posts.apps.PostsConfig"
```
