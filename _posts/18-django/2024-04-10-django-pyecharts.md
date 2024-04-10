---
layout:        post
title:         "Django | Django项目嵌入pyecharts图表"
subtitle:      "python + Django + pyecharts + scikit-learn"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Django
    - Python
---

### 背景
&emsp;&emsp;在 Django 项目中，如果你想要将 pyecharts 生成的图表渲染成字符串并在模板中显示，你需要使用 pyecharts 提供的 render_embed() 方法，这个方法可以生成一个包含图表 HTML 代码的字符串。然后，你可以将这个字符串传递给 Django 模板进行渲染。

<br>
<br>

### 步骤说明
1、安装pyecharts库（如果你还没有安装的话）：           
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts==1.9.0
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Django==4.2.11
```

<br>
<br>

2、在你的 Django 视图中，使用 pyecharts 创建图表，并使用 render_embed() 方法获取 HTML 字符串：                
```python
from django.shortcuts import render
from pyecharts.charts import Bar
from pyecharts import options as opts

def chart_view(request):
    # 创建一个柱状图对象
    bar = Bar()
    bar.add_xaxis(["A", "B", "C", "D", "E"])
    bar.add_yaxis("Series A", [5, 20, 36, 10, 10])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="My Bar Chart"))

    # 渲染图表为HTML字符串
    chart_html = bar.render_embed()

    # 将HTML字符串传递给模板
    return render(request, "my_template.html", {"chart_html": chart_html})
```

<br>
<br>

3、在你的 Django 模板 charts.html 中，插入这个 HTML 字符串：             
&emsp;&emsp;注意，在模板中，我们使用 `{{ chart_html|safe }}` 来确保 Django 不会转义 HTML 代码。如果不使用 safe 过滤器，Django 将会转义 HTML 标签，导致图表无法正确显示。                
```html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Chart</title>
    <!-- 引入pyecharts的JavaScript库 -->
    <script src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
</head>
<body>
    <!-- 使用safe过滤器来避免Django模板引擎转义HTML代码 -->
    {{ chart_html|safe }}
</body>
</html>
```

<br>
<br>

4、确保你的 Django 项目已经配置好了 URL 路由，以便能够通过 URL 访问到这个视图。            
```python
from django.urls import re_path as url, include, path
from . import views

urlpatterns = [
    path('', views.index),
    url('index/', views.index),
    url('home/', views.home),
    url('add/', views.add),
    url('edit/', views.edit),
    url('delete/', views.delete),
    # url('chart/', views.to_charts),
    url('me/', views.to_me),
    url('borrow/', views.index_borrow),
    url('chart/', views.chart_view, name='chart')
]
```

<br>
<br>

---

参考项目：        
[基于Django的图书管理系统](https://gitee.com/haauleon/book_system)           
[django项目中pyecharts详细使用教程1](https://blog.csdn.net/weixin_42289273/article/details/109579542)