# week06 Django

学习笔记<br />

<a name="6623cc97"></a>
### Django 框架


<a name="e05dce83"></a>
#### 简介
Django是一个开放源代码的Web应用框架<br />最初用于管理一些以新闻内容为主的网站(CMS)<br />2005年7月再BSD许可证下发布<br />

<a name="hPGXE"></a>
#### 特点

- 采用了MTV的框架
- 强调快速开发和代码复用DRY(Do Not Repeat Yourself)
- 组件丰富:

ORM(对象关系映射)映射类来构建数据模型<br />URL支持正则表达式<br />模板可继承<br />内置用户认证,提供用户认证和权限功能<br />admin管理系统<br />内置表单模型,Cache缓存系统,国际化系统等<br />
<br />pip install django==2.2.13<br />

<a name="3704b620"></a>
#### MTV 框架模式

- 模型 (Model)
- 模板 (Template)
- 视图 (Views)


<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/1422780/1596339637767-d76b495a-c410-433c-87f7-b5935c68f771.png#align=left&display=inline&height=311&margin=%5Bobject%20Object%5D&name=image.png&originHeight=311&originWidth=762&size=21166&status=done&style=none&width=762)<br />

<a name="rVQYB"></a>
#### 创建Django项目
$ django-admin startproject MyDjango<br />
<br />

<a name="fddEt"></a>
#### 创建Django应用程序
$ python manage.py help  查看该工具的具体功能<br />
<br />$ python manage.py startapp index<br />index/migrations   数据库迁移文件夹<br />index/models.py   模型<br />index/apps.py       当前app配置文件<br />index/admin.py     管理后台<br />index/tests.py       自动化测试<br />index/views.py      视图<br />

<a name="rBHrs"></a>
#### 启动和停止Django应用程序
$ python manage.py runserver   启动  默认是127.0.0.1:8000
> 问题: 运行时无反应(windows环境)
> 删除_manage.py_中的_ #!/usr/bin/env python_


<br />$ python manage.py runserver 0.0.0.0:80<br />
<br />Quit the server with CONTROL-C  /  Quit the server with CTRL-BREAK(我)<br />$CONTROL-C  /  CTRL-BREAK(我)

<a name="1JT8e"></a>
#### Django的配置文件

- 项目路径
- 密钥
- 域名访问权限
- App列表
- 静态资源,包括CSS,JavaScript图片等
- 模板文件
- 数据库配置
- 缓存
- 中间件


<br />

