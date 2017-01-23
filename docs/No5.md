# NO.5 model to admin
一行代码让model在admin中可见

## 先做以下五步：

    1. 去掉models.py里面 把class Posts改成 class Post
    2. 在__str__(self) __unicode__(self)
    3. python .\manage.py makemigrations
    4. y/n--> y
    5. python .\manage.py migrate


## admin.py
```
from posts import models

admin.site.register(models.Post)

```
