# NO.4 Django App and Model

## Django中project和app分别是什么？
Project：python manage.py startproject 你的project名
app: python manage.py startapp 你的app名字
project是项目，project下面分一个或多个app


## 我们的第一个App

```
python manage.py startapp app的名字
```

## 一定要注意：
把你的app在project的settings.py里面的INSTALLED_APPS加上

## Model
models.py里面创建类（与数据库建立联系的）

```
python manage.py makemigrations（告诉Django我设计了一些表结构，你去准备一下）

python manage.py migrate（告诉Django去数据库里操作一下刚才的动作）
```
