---
layout:        post
title:         "Pytest | allure 美化"
subtitle:      "定制化输出测试报告"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - Allure
    - Pytest
    - 单元测试框架
---



### 一、定制化后的效果展示
用两张图展示效果：       
![](\img\in-post\post-python\2023-06-20-python-allure-1.png)       

![](\img\in-post\post-python\2023-06-20-python-allure-2.png)      

<br>
<br>

### 二、注意别踩坑
&emsp;&emsp;allure 定制化想必大部分情况都会去选择 `pip install pytest-allure-adaptor` 这个插件，安装完成后，运行定制化代码出现以下报错：    
![](\img\in-post\post-python\2023-06-20-python-allure-3.png)       

<br>

&emsp;&emsp;安装了 `pytest-allure-adaptor` 插件的定制代码像这样的：        
![](\img\in-post\post-python\2023-06-20-python-allure-4.png)       

<br>

&emsp;&emsp;我们会使用 `allure.MASTER_HELPER` 下的方法去进行定制，通过查看该插件的官网 [http://pypi.org/project/pytest-allure-adaptor/](http://pypi.org/project/pytest-allure-adaptor/)，发现版本不匹配，因此抛出了异常：    
![](\img\in-post\post-python\2023-06-20-python-allure-5.png)       

<br>

解决办法：     
- pytest-allure-adaptor 版本过低不兼容当前版本的 allure，选择不安装该插件   
- 使用 allure 下的方法去进行定制

<br>
<br>

### 三、定制化内容
使用前，先引入 allure 模块     
```python
import allure
```

<br>

#### 1.feature-测试用例特性（主要功能模块）
使用方法：    
```python
@allure.feature()
```
![](\img\in-post\post-python\2023-06-20-python-allure-6.png)       

![](\img\in-post\post-python\2023-06-20-python-allure-7.png)       

![](\img\in-post\post-python\2023-06-20-python-allure-8.png)       

<br>

#### 2.story-feature功能模块下的分支功能
使用方法：     
```python
@allure.story()
```
![](\img\in-post\post-python\2023-06-20-python-allure-9.png)        

![](\img\in-post\post-python\2023-06-20-python-allure-10.png)       

<br>

#### 3.severity-测试用例的严重级别
Allure 中对严重级别的定义：      
- blocker 级别：中断缺陷（客户端程序无响应，无法执行下一步操作）     
- critical 级别：临界缺陷（ 功能点缺失）    
- normal 级别：普通缺陷（数值计算错误）   
- minor 级别：次要缺陷（界面错误与UI需求不符）    
- trivial 级别：轻微缺陷（必输项无提示，或者提示不规范）


使用方法：     
```python
@allure.severity(allure.severity_level.CRITICAL)
@allure.severity('critical')
```
![](\img\in-post\post-python\2023-06-20-python-allure-11.png)        

![](\img\in-post\post-python\2023-06-20-python-allure-12.png)       

<br>

#### 4.step-测试用例的步骤
使用方法：    
```python
@allure.step()  # 只能以装饰器的形式放在类或者方法上面　　   
with allure.step():  # 可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
```
![](\img\in-post\post-python\2023-06-20-python-allure-13.png)        

![](\img\in-post\post-python\2023-06-20-python-allure-14.png)       

<br>

#### 5.attach-用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
使用方法：    
```python
allure.attach(body, name, attachment_type, extension)
```

- body - 要写入文件的原始内容
- name - 包含文件名的字符串
- attachment_type - 其中一个allure.attachment_type值
- extension - 提供的将用作创建文件的扩展名

![](\img\in-post\post-python\2023-06-20-python-allure-15.png)        

![](\img\in-post\post-python\2023-06-20-python-allure-16.png)       

<br>

#### 6.link/issue/testcase-链接
使用方法：     
```python
@allure.link()
@allure.issue()
@allure.testcase()
```

![](\img\in-post\post-python\2023-06-20-python-allure-17.png)        

![](\img\in-post\post-python\2023-06-20-python-allure-18.png)       

<br>

#### 7.description-用例描述
使用方法：      
```python
@allure.description()  # 提供描述字符串的装饰器
@allure.description_html()  # 提供一些HTML在测试用例的描述部分
```
![](\img\in-post\post-python\2023-06-20-python-allure-19.png)        

![](\img\in-post\post-python\2023-06-20-python-allure-20.png)       

<br>

#### 8.title-重命名测试用例
报告中的用例名称默认显示的是函数英文名，可以使用 title 重命名为中文：    
```python
    @allure.title("登录成功场景-{data}")
    @pytest.mark.parametrize("data", login_success_data, ids=ids_login_success_data)
    def test_login_success(self, data):
        """测试登录成功"""
        user = input_username(data["user"])
        pwd = input_password(data["pwd"])
        result = login(user, pwd)
        assert result == data["expected"]
```
![](\img\in-post\post-python\2023-06-20-python-allure-21.png)       

<br>
<br>

---

相关链接：    
[pytest-allure美化——定制化输出测试报告](https://blog.csdn.net/IT_LanTian/article/details/124018836)