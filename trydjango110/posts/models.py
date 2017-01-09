from django.db import models

# Create your models here.

# MVC框架
# Model View Controllers
# MTV <-> Django
# Model View Template

# ORM
# 跟数据库相关的

# 帖子
class Post(models.Model):

    title = models.CharField(max_length=256)  # 标题，存文字的
    content = models.TextField()  # 内容
    update = models.DateTimeField(auto_now=True, auto_now_add=False)  # 更新的时间戳
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)  # 创建时的时间戳

    def __str__(self):  # Python3
        return self.title

    def __unicode__(self):  # Python2
        return self.title
