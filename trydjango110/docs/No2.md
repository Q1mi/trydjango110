# NO.2 第一个Django程序


## 补充
如何让PowerShell中的当前路径只显示最后的目录？（C:\folder\directory\name> ==> name>）

### 在PowerShell中进行如下操作：
    1. Test-Path $profile（如果返回的是True，跳过第2步）
    2. New-Item -path $profile -type file –force（返回 ‘XX:\Documents\xxxxxx\PERSONNEL\WindowsPowerShell\Microsoft.PowerShell_profile.ps1’ is now created, so let’s open it (newly created, the file is empty).）
    3. $profile（输出文件的位置）
    4. 使用notepad++或者sublime text等打开上面的文件
    5. 粘贴如下代码：

    ```
    function prompt {
      $p = Split-Path -leaf -path (Get-Location)
      "$p> "
    }
    ```
    6. 重启PowerShell


## 正题

    1. Sublime Text 3打开项目所在路径
    2. 命令行创建新的project，大致看一下目录结构
    3. 修改上层文件名为src，简单介绍一下why do this
    4. python .\manage.py makemigrations
    5. python .\manage.py migrate 简单介绍一下这两个命令的作用
    6. 简单介绍一下settings.py中的内容
    7. python .\manage.py createsuperuser
    8. python .\manage.py runserver
    9. Django Admin初见
