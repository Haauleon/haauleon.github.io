---
layout:        post
title:         "Python3 | cron 表达式中的 ?"
subtitle:      "Cron 表达式中 ? 以及周的部分用法"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### Cron表达式关于?号的使用
1. Seconds （秒）      
2. Minutes（分）     
3. Hours（小时）       
4. Day-of-Month （天）     
5. Month（月）     
6. Day-of-Week （周）        
7. Year（年）         

Cron 表达式的格式：秒 分 时 日 月 周 年(可选)     

? ：用在 Day-of-Month 和 Day-of-Week 中，指“没有具体的值”。     

当两个子表达式其中一个被指定了值以后，为了避免冲突，需要将另外一个的值设为“?”。        
例如：想在每月 10 日触发调度，不管 10 号是星期几，只能用如下写法：    
```
0 0 0 10 * ?
```
其中最后以为只能用 `?`，而不能用 `*`。 即为了避免冲突 `?` 只能放在第 4 或第 6 的位置上            
注意：一般 cron 表达式写六位就行


<br>
<br>

### Cron表达式中周的部分用法
其中 1-7 表示的含义，注意：1 代表的是星期日         
```java
public final static int SUNDAY = 1;
public final static int MONDAY = 2;
public final static int TUESDAY = 3;
public final static int WEDNESDAY = 4;
public final static int THURSDAY = 5;
public final static int FRIDAY = 6;
public final static int SATURDAY = 7;
```

例如：想要每小时执行一次只在周一到周五执行，这就是一个错误的 cron 表达式：                     
```
0 0 0/1 ? * 1-5
```     

正确的cron表达式：           
```
0 0 0/1 ? * 2-6
```

或者是：    
```
0 0 0/1 ? * MON-FRI
```

注意：如果你的 cron 表达式是写在 yml 文件中的，一定要在冒号（：）后面                 
使用一个空格，否则表达式不会生效     

<br>
<br>

---

相关链接：   
[Cron表达式中“?“以及周的部分用法](https://blog.csdn.net/qq_45256805/article/details/107849309)
