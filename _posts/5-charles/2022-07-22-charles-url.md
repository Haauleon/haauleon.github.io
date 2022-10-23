---
layout:        post
title:         "Charles | URL 映射"
subtitle:      "使用 Charles 拦截项目接口映射请求本地或映射远程地址URL"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Charles
    - API 测试
---

### 一、为什么要把接口数据配置到本地json文件里？
相信有很多跟我一样的前端同学遇到：       
- 很久之前【公司项目】无法启动，原因接口请求不到了（权限给你踢了，服务器换了等）
- 【面试的时候】，需要展示之前做过的项目（用来证明自己）
- 自己查阅之前开发的功能时，需要 run 起来项目

<br>

不依赖线上接口数据好处：        
- 【更灵活的假数据】，可用于开发时，提前渲染还没有的接口
- 【前后端分离并行开发】，可以对照后端 1 比 1 写好一个 json 文件
- 【很久的项目也能跑起来】，项目不管多久后，单机都能跑起来，方便自己找之前的方法和功能

<br>
<br>

### 二、配置 URL 映射
Charles 可以映射到本地 Map Local 或 映射远程地址URL Map Remote。    

###### 1、配置Map Remote
配置 `Map Remote` 映射到自己的本地地址或域名 `eg: 127.0.0.1 || myself.domain.host`。    

1. 打开：`Tools -> Map Remote Settings`            
    ![](\img\in-post\post-charles\2022-07-22-charles-url-1.png)      
    ![](\img\in-post\post-charles\2022-07-22-charles-url-2.png)     
2. 配置 Map Remote 时，自己写的单入口文件处理返回指定的 json，脚本：    
    ```
    <?php
    // Set Header (设置后前端无需转义直接获取 json 格式的数据)
    header("Content-Type:application/json");

    const DEBUG = false;

    // Get Entry File Name (/index.php)
    !DEBUG ?: var_dump($_SERVER['SCRIPT_NAME']);
    // Get REQUEST_UR (获取请求路径 /index.phpv2/user/info)
    !DEBUG ?: var_dump($_SERVER['REQUEST_URI']);
    // Remove SCRIPT_NAME
    !DEBUG ?: var_dump(str_replace($_SERVER['SCRIPT_NAME'], '', $_SERVER['REQUEST_URI']));
    $fileName = str_replace($_SERVER['SCRIPT_NAME'], '', $_SERVER['REQUEST_URI']) . '.json';
    // Replace "/" to ":" (这样才能找到带'/'的字符串文件名)
    $fileName = str_replace('/', ':', $fileName);
    !DEBUG ?: var_dump('fileName ->' . $fileName);

    // Require
    @$json = include('./'. $fileName);
    if (!$json) {
        $json = include('./500.json');
    }
    !DEBUG ?: var_dump('$json ->' . $json);

    return json_encode($json);

    ?>
    ```

<br>

###### 2、配置Map Local
配置 `Map Local` 映射到本地 json。    

1. 打开：`Tools -> Map Local Settings`       
    ![](\img\in-post\post-charles\2022-07-22-charles-url-3.png)     
    ![](\img\in-post\post-charles\2022-07-22-charles-url-4.png)         
2. 去创建一个 json ，文件内容如下，目的就是如上图 Map To 要映射的数据 json             
    ![](\img\in-post\post-charles\2022-07-22-charles-url-5.png)

<br>

###### 3、配置跨域请求
配置跨域请求（不是映射的 https 不需要配置），如果是映射像我上面 https 接口地址的话就会有跨域问题（浏览器同源策略）。        

1. 打开：`Tools -> Rewrite Settings`      
    ```
    Access-Control-Allow-Origin:http://localhost:8083
    Access-Control-Allow-Methods:GET,POST,OPTIONS,PUT
    Access-Control-Allow-Headers:Accept,Origin,X-Requested-With,Content-Type,Last-Modified
    Allow:GET,HEAD,POST,PUT,DELETE,TRACE,OPTIONS,PATCH
    404->200 // 特殊选择：Rewrite Rule 的 Type 选择 Response Status
    Access-Control-Allow-Credentials:true
    ```
    ![](\img\in-post\post-charles\2022-07-22-charles-url-6.png)      
    ![](\img\in-post\post-charles\2022-07-22-charles-url-7.png)
2. 大功告成，验证一下！    
    然后正常项目请求接口，打印 res 查看一下就能看到之前定义的 json 文件里的数据      
    ![](\img\in-post\post-charles\2022-07-22-charles-url-8.png)

<br>
<br>

### 三、扩展内容
###### 1、配置证书
安装证书（只是针对 https 域名 443，因为 443 是加密的，http 不需要），如果不安装和不信任证书 443 安全域名会加锁，会映射不到接口。            

1. 打开：`Help -> SSL Proxying -> Install Charles Root Certificate`        
    ![](\img\in-post\post-charles\2022-07-22-charles-url-9.png)      
    ![](\img\in-post\post-charles\2022-07-22-charles-url-10.png)

<br>

###### 2、配置代理设置
需要注意的是，配置 `*` 时，所有网页接口都会被拦截包括百度简书等，以及你正在使用的浏览器上的所有页面。     

1. 打开：`Proxy -> SSL Proxying Settings`      
    ![](\img\in-post\post-charles\2022-07-22-charles-url-11.png)

<br>
<br>

### 四、遇到的问题
###### 1、软件权限问题     
软件权限问题 (请确保 Charles 在可读写的卷上运行)     
```
Charles cannot configure your proxy settings while it is on a read-only volume. Perhaps you are running Charles from the disk image? If so, please copy Charles to the Applications folder and run it again. Otherwise please ensure that Charles is running on a volume that is read-write and try again.
```

<br>

解决配置上面说 `Rewrite Settings` 跨域问题。     
```
sudo chown -R root "/Applications/Charles.app/Contents/Resources"
sudo chmod -R u+s "/Applications/Charles.app/Contents/Resources"
```

<br>

###### 2、跨域问题
跨域问题 Access-Control-Allow-Origin。    
```
Access to XMLHttpRequest at 'https://api.huoban.com/v2/ticket/parse' from origin 'http://localhost:8083' has been blocked by CORS policy: The value of the 'Access-Control-Allow-Origin' header in the response must not be the wildcard '*' when the request's credentials mode is 'include'. The credentials mode of requests initiated by the XMLHttpRequest is controlled by the withCredentials attribute.
```

![](\img\in-post\post-charles\2022-07-22-charles-url-12.png)        

<br>

解决配置上面说 Rewrite Settings 跨域问题。       
```
Access-Control-Allow-Origin:http://localhost:8083
```

![](\img\in-post\post-charles\2022-07-22-charles-url-13.png)     

<br>

###### 3、跨域问题
跨域问题 Access-Control-Allow-Credentials。     
```
Access to XMLHttpRequest at 'https://api.xxxxxx.com/v2/ticket/parse' from origin 'http://localhost:8083' has been blocked by CORS policy: The value of the 'Access-Control-Allow-Credentials' header in the response is '' which must be 'true' when the request's credentials mode is 'include'. The credentials mode of requests initiated by the XMLHttpRequest is controlled by the withCredentials attribute.
```     

![](\img\in-post\post-charles\2022-07-22-charles-url-14.png) 

<br>

解决配置上面说 Rewrite Settings 跨域问题。    
```
Access-Control-Allow-Credentials:true
```

![](\img\in-post\post-charles\2022-07-22-charles-url-15.png) 

---
以上参考自 [https://www.jianshu.com/p/b1a798079813](https://www.jianshu.com/p/b1a798079813)