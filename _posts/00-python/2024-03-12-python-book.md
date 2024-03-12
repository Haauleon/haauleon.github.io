---
layout:        post
title:         "爬虫 | 豆瓣读书、当当网图书排行榜"
subtitle:      "爬取豆瓣读书畅销榜TOP250和当当网图书排行榜TOP500"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 背景
&emsp;&emsp;最近在帮我弟爬一些数据，仅此而已~

<br>
<br>

### 代码实现
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
"""
import requests
from lxml import etree
from enum import  Enum


headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# 当当网页面元素枚举
class DDWPageEle(Enum):
    ele_names = '//div[2]/ul/li/div[3]/a/@title'
    ele_comments = '//div[2]/ul/li/div[4]/a/text()'
    ele_fivestars = '//div[2]/ul/li/div[7]/span/text()'


# 豆瓣读书网页面元素枚举
class DBPageEle(Enum):
    ele_names = '//table/tr/td[2]/div[1]/a/@title'
    ele_authors = '//table/tr/td[2]/p[1]/text()'
    ele_comments = '//table/tr/td[2]/div[2]/span[3]/text()'



class DangDangWang:

    def __init__(self):
        self.headers = headers
        self.names = None
        self.comments = None
        self.fivestars = None

    def get_book_info(self, url):
        """获取当当网图书排行榜"""
        res = requests.get(url, headers=self.headers)
        res.encoding = res.apparent_encoding  # 将乱码进行编码
        html = etree.HTML(res.text)
        for book in html:
            self.names = book.xpath(DDWPageEle.ele_names.value)
            self.comments = book.xpath(DDWPageEle.ele_comments.value)
            self.fivestars = book.xpath(DDWPageEle.ele_fivestars.value)

        for name, comment, fivestar in zip(self.names, self.comments, self.fivestars):
            yield name, comment, fivestar


class DouBan:

    def __init__(self):
        self.headers = headers
        self.names = None
        self.authors = None
        self.comments = None

    def get_book_info(self, url):
        """获取豆瓣读书排行榜"""
        res = requests.get(url, headers=self.headers)
        html = etree.HTML(res.text)
        for book in html:
            self.names = book.xpath(DBPageEle.ele_names.value)
            self.authors = book.xpath(DBPageEle.ele_authors.value)
            self.comments = book.xpath(DBPageEle.ele_comments.value)

        for name, author, comment in zip(self.names, self.authors, self.comments):
            yield name.strip(), author.split('/')[0].strip(), comment.replace('(', '').replace(')', '').strip()


def run_ddw_spider():
    """执行爬取当当网图书数据"""
    urls = ['http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-{}'.format(i) for i in range(1,26)]
    ddw = DangDangWang()
    rank = 1
    for url in urls:
        print(url)
        for name, comment, fivestar in ddw.get_book_info(url):
            print(rank, name, comment, fivestar)
            rank += 1


def run_db_spider():
    """执行爬取豆瓣图书数据"""
    urls = ['https://book.douban.com/top250?start={}'.format(i*25) for i in range(10)]
    db = DouBan()
    rank = 1
    for url in urls:
        print(url)
        for name, author, comment in db.get_book_info(url):
            print(rank, name, author, comment)
            rank += 1


if __name__=='__main__':
    run_ddw_spider()
    print('-'*50)
    run_db_spider()

```

<br>
<br>

### 爬取结果
```txt
C:\Users\EJET\AppData\Local\Programs\Python\Python38\python.exe C:/Users/EJET/AppData/Roaming/JetBrains/PyCharm2020.1/scratches/scratch_10.py
http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1
1 国货崛起：传统品牌如何突围 3050条评论 3046次
2 夺取群星：全三册（雨果奖得主布兰登・桑德森科幻力作，沉浸式热血空战物语） 1103条评论 1073次
3 天工开物（中国17世纪的工艺百科全书）全注全译版 8434条评论 6014次
4 管理者20法则：看清领导力的底层逻辑 2603条评论 2041次
5 财富的底层逻辑 2485条评论 2056次
6 历史的镜子（中国史学大家吴晗经典作品） 6765条评论 4361次
7 就算颠沛流离，也要风生水起 1047条评论 1040次
8 聊斋志异（全注释文白对照版）蒲松龄中国古代志怪小说经典 2259条评论 2054次
9 水浒传（全3册）中国古典文学四大名著 原著无删足回正版 2162条评论 2110次
10 鲁滨逊漂流记（经典全译本） 1059条评论 1039次
11 钢铁是怎样炼成的 2297条评论 2027次
12 梦中的暗杀者（梦中的杀手竟造成了真实的死亡，世界的崩溃由此开始！人称“鬼才”的小林泰三，推理迷期待已久的烧脑神作终于来了！） 1438条评论 1030次
13 西游记（全3册）中国古典文学四大名著 无障碍阅读 原著无删 2630条评论 2512次
14 小窗幽记（与菜根谭围炉夜话并称处世三大奇书） 21018条评论 14711次
15 从一到无穷大（爱因斯坦亲笔推荐的科普入门书，清华大学校长送给新生的礼物） 13195条评论 7480次
16 王阳明传 52159条评论 13709次
17 致女儿书 548条评论 551次
18 正向对话:提升人际关系的非暴力沟通宝典，畅销全球12国 550条评论 550次
19 父母：挑战 550条评论 550次
20 婚姻：挑战 551条评论 550次
http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-2
21 雪国【当当定制雪国美景明信片】川端康成50周年纪念版 11037条评论 6549次
22 心理学的100个基本（口袋里的心理学指南） 4621条评论 1644次
23 向上管理：与你的领导相互成就 121284条评论 61136次
......
--------------------------------------------------
https://book.douban.com/top250?start=0
1 红楼梦 [清] 曹雪芹 著 420492人评价
2 活着 余华 824576人评价
3 1984 [英] 乔治·奥威尔 281520人评价
4 哈利·波特 J.K.罗琳 (J.K.Rowling) 104553人评价
5 三体全集 刘慈欣 184452人评价
6 百年孤独 [哥伦比亚] 加西亚·马尔克斯 421712人评价
7 飘 [美国] 玛格丽特·米切尔 211064人评价
8 房思琪的初恋乐园 林奕含 375048人评价
9 动物农场 [英] 乔治·奥威尔 158011人评价
10 三国演义（全二册） [明] 罗贯中 167032人评价
11 福尔摩斯探案全集（上中下） [英] 阿·柯南道尔 132494人评价
12 白夜行 [日] 东野圭吾 469490人评价
13 小王子 [法] 圣埃克苏佩里 751676人评价
14 安徒生童话故事集 （丹麦）安徒生 131543人评价
15 撒哈拉的故事 三毛 172473人评价
16 天龙八部 金庸 132055人评价
17 呐喊 鲁迅 158776人评价
18 杀死一只知更鸟 [美] 哈珀·李 145034人评价
19 悉达多 [德] 赫尔曼·黑塞 98838人评价
20 明朝那些事儿（1-9） 当年明月 171911人评价
21 邓小平时代 【美】傅高义 (Ezra.F.Vogel) 69037人评价
22 失踪的孩子 [意] 埃莱娜·费兰特 79656人评价
23 新名字的故事 [意] 埃莱娜·费兰特 90244人评价
24 沉默的大多数 王小波 150236人评价
25 野草 鲁迅 46617人评价
https://book.douban.com/top250?start=25
26 中国历代政治得失 钱穆 71752人评价
27 局外人 [法] 阿尔贝·加缪 237081人评价
28 人类简史 [以色列] 尤瓦尔·赫拉利 198007人评价
......

Process finished with exit code 0

```