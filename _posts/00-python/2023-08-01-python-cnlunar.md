---
layout:        post
title:         "Python3 | 获取旧历农历老黄历"
subtitle:      "python 获取节假日，二十四节气，中国农历，星次、每日凶煞、每日值神、农历建除十二神等"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 前言
1、不使用寿星通式 `[Y*D+C]-L`，而使用香港天文台数据（阴阳合历，节气准农历日期才能准）       
2、无数据库，依赖库少，运行快速，提供内容丰富          
3、主要内容来自于《钦定协纪辨方书》，每一个神煞宜忌都有依据，遵循宜忌等第表，包含民用、御用事宜，且支持港式（通书配图）八字月柱算法-默认，通书原文文字农历月份算法，具体看 demo.py         
4、不盈利，开源免费，长期有人维护            
5、民俗社会科学项目，不搞封建迷信，宜忌意义在于民间是将红白事合理分开，避免今日您宴请宾客，邻居办白事情况出现，引起邻里纠纷社会分裂。              

<br>
<br>

### 一、cnlunar是什么？
cnlunar 是中国农历历法项目，无需数据库环境，以《钦定协纪辨方书》为核心的 python3 农历、黄历、二十四节气、节假日、星次、每日凶煞、每日值神、农历建除十二神、农历每日宜忌、彭祖百忌、每日五行、二十八星宿、天干地支、农历生辰八字、时辰凶吉等开源项目。

<br>
<br>

### 二、使用步骤
#### 1.安装pip第三方包
```bash
$ pip3 install cnlunar~=0.1.1
```

<br>

#### 2.使用
```python
import datetime
import cnlunar

a = cnlunar.Lunar(datetime.datetime(2022, 11, 14, 10, 30), godType='8char')  # 常规算法
# a = cnlunar.Lunar(datetime.datetime(2022, 2, 3, 10, 30), godType='8char', year8Char='beginningOfSpring')  # 八字立春切换算法
dic = {
    '日期': a.date,
    '农历数字': (a.lunarYear, a.lunarMonth, a.lunarDay, '闰' if a.isLunarLeapMonth else ''),
    '农历': '%s %s[%s]年 %s%s' % (a.lunarYearCn, a.year8Char, a.chineseYearZodiac, a.lunarMonthCn, a.lunarDayCn),
    '星期': a.weekDayCn,
    # 未增加除夕
    '今日节日': (a.get_legalHolidays(), a.get_otherHolidays(), a.get_otherLunarHolidays()),
    '八字': ' '.join([a.year8Char, a.month8Char, a.day8Char, a.twohour8Char]),
    '今日节气': a.todaySolarTerms,
    '下一节气': (a.nextSolarTerm, a.nextSolarTermDate, a.nextSolarTermYear),
    '今年节气表': a.thisYearSolarTermsDic,
    '季节': a.lunarSeason,

    '今日时辰': a.twohour8CharList,
    '时辰凶吉': a.get_twohourLuckyList(),
    '生肖冲煞': a.chineseZodiacClash,
    '星座': a.starZodiac,
    '星次': a.todayEastZodiac,

    '彭祖百忌': a.get_pengTaboo(),
    '彭祖百忌精简': a.get_pengTaboo(long=4, delimit='<br>'),
    '十二神': a.get_today12DayOfficer(),
    '廿八宿': a.get_the28Stars(),

    '今日三合': a.zodiacMark3List,
    '今日六合': a.zodiacMark6,
    '今日五行': a.get_today5Elements(),

    '纳音': a.get_nayin(),
    '九宫飞星': a.get_the9FlyStar(),
    '吉神方位': a.get_luckyGodsDirection(),
    '今日胎神': a.get_fetalGod(),
    '神煞宜忌': a.angelDemon,
    '今日吉神': a.goodGodName,
    '今日凶煞': a.badGodName,
    '宜忌等第': a.todayLevelName,
    '宜': a.goodThing,
    '忌': a.badThing,
    '时辰经络': a.meridians
}
for i in dic:
    midstr = '\t' * (2 - len(i) // 2) + ':' + '\t'
    print(i, midstr, dic[i])
```

<br>

输出：   
```bash
日期 	:	 2022-11-14 10:30:00
农历数字 :	 (2022, 10, 21, '')
农历 	:	 二零二二 壬寅[虎]年 十月大廿一
星期 	:	 星期一
今日节日 :	 ('', '', '')
八字 	:	 壬寅 辛亥 辛未 癸巳
今日节气 :	 无
下一节气 :	 ('小雪', (11, 22), 2022)
今年节气表 :	 {'小寒': (1, 5), '大寒': (1, 20), '立春': (2, 4), '雨水': (2, 19), '惊蛰': (3, 5), '春分': (3, 20), '清明': (4, 5), '谷雨': (4, 20), '立夏': (5, 5), '小满': (5, 21), '芒种': (6, 6), '夏至': (6, 21), '小暑': (7, 7), '大暑': (7, 23), '立秋': (8, 7), '处暑': (8, 23), '白露': (9, 7), '秋分': (9, 23), '寒露': (10, 8), '霜降': (10, 23), '立冬': (11, 7), '小雪': (11, 22), '大雪': (12, 7), '冬至': (12, 22)}
季节 	:	 孟冬
今日时辰 :	 ['戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳', '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子']
时辰凶吉 :	 ['凶', '凶', '吉', '吉', '凶', '吉', '凶', '凶', '吉', '凶', '吉', '吉', '吉']
生肖冲煞 :	 羊日冲牛
星座 	:	 天蝎座
星次 	:	 析木
彭祖百忌 :	 辛不合酱 主人不尝,未不服药 毒气入肠
彭祖百忌精简 :	 辛不合酱<br>未不服药
十二神 	:	 ('成', '明堂', '黄道日')
廿八宿 	:	 张月鹿
今日三合 :	 ['猪', '兔']
今日六合 :	 马
今日五行 :	 ['天干', '辛', '属金', '地支', '未', '属土', '纳音', '土', '属土', '廿八宿', '张', '宿', '十二神', '成', '日']
纳音 	:	 路旁土
九宫飞星 :	 513468927
吉神方位 :	 ['喜神西南', '财神正东', '福神西北', '阳贵东北', '阴贵正南']
今日胎神 :	 厨灶厕外西南
神煞宜忌 :	 ((['三合', '六仪', '不守塚', '临日', '天喜', '福生', '月财'], ['厌对', '招摇', '往亡', '神号', '四击', '义日']), (['祭祀', '结婚姻', '宴会', '修造', '入学', '竖柱上梁', '经络', '开市', '纳财', '安碓硙', '破土', '筑堤防', '纳畜', '裁制', '庆赐', '修仓库', '缮城郭', '纳采', '修宫室', '祈福', '立券交易'], ['求医疗病', '捕捉', '畋猎', '取鱼', '宣政事', '整手足甲', '选将', '出师', '乘船渡水', '颁诏', '招贤']))
今日吉神 :	 ['三合', '六仪', '不守塚', '临日', '天喜', '福生', '月财']
今日凶煞 :	 ['厌对', '招摇', '往亡', '神号', '四击', '义日']
宜忌等第 :	 无
宜 		:	 ['祭祀', '结婚姻', '宴会', '修造', '入学', '竖柱上梁', '经络', '开市', '纳财', '安碓硙', '破土', '筑堤防', '纳畜', '裁制', '庆赐', '修仓库', '缮城郭', '纳采', '修宫室', '祈福', '立券交易']
忌 		:	 ['求医疗病', '捕捉', '畋猎', '取鱼', '宣政事', '整手足甲', '选将', '出师', '乘船渡水', '颁诏', '招贤']
时辰经络 :	 脾
```

<br>
<br>

### 总结
本文仅仅简单介绍了 cnlunar 的使用，而 cnlunar 提供了大量的日历数据。     
项目地址：[https://github.com/OPN48/cnlunar](https://github.com/OPN48/cnlunar)     

<br>
<br>

---

相关链接：   
[python 获取节假日，二十四节气，中国农历，星次、每日凶煞、每日值神、农历建除十二神、农历每日宜忌、彭祖百忌、每日五行、二十八星宿、天干地支、农历生辰八字、时辰凶吉等](https://blog.csdn.net/weixin_41486438/article/details/128382301)