# NO.1 Virtualenv&Django

    1. 环境要求

        1. Windows
        2. Python3.5+

    2. 需要技能

        1. 基础的Python语法
        2. 基本的命令行操作

    3. 配置虚拟环境

        1. 安装virtualenv： pip install virtualenv
        2. 使用virtualenv

            1. 创建虚拟环境：virtualenv 虚拟环境（文件夹）名
            2. 启用虚拟环境：scripts\activate
            3. 退出虚拟环境：deactivate

    4. 安装Django

        1. pip install django

    5. 第一个Django项目

        1. python manage.py startproject my_first（我们的项目名）
        2. python manage.py runserver 

补充：

    1. PowerShell里面执行activate失败？
        输入：set-executionpolicy RemoteSigned

    2. pip freeze 命令使用

        1. pip freeze > requirements.txt （保存依赖包到requirements.txt）
        2. pip install -r requirements.txt （批量安装项目需要的所有依赖包）


