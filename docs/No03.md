# NO.3 Django Admin补充

## 上节错误纠正

WSGI(Web  server gateway interface)：Web服务器网关接口是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。自从WSGI被开发出来以后，许多其它语言中也出现了类似接口。

web server(nginx/tomcat) <-WSGI-> web app(我们写的Python代码)


## createsuperuser

    1. python manage.py createsuperuser
    2. 注意事项，至少八个字符，不能是简单的数字
    3. Django admin使用的介绍
        1. python manage.py runserver 127.0.0.1:8000
        2. 浏览器里面输入：http://127.0.0.1:8000/admin/
        3. 输入用户名、密码登录即可。

## urls.py介绍 

主要实现路由控制的功能
