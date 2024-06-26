---
layout:        post
title:         "项目复盘 | 农村电商一村一品"
subtitle:      "微信小程序 + 后台管理系统"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 面试
---

## 一、项目概况

<table border="2" style="border-collapse: collapse;">
    <tr>
       <th>复盘项目名称</th>
       <td>农村电商一村一品小程序</td>
    </tr>
    <tr>
        <th>产品版本号</th>
        <td>V 1.0.0</td>
    </tr>
    <tr>
        <th>上线时间</th>
        <td>2021 年 7 月 12 日</td>
    </tr>
    <tr>
        <th>复盘事件</th>
        <td>2021 年 7 月 16 日</td>
    </tr>
</table>

<br><br>


## 二、回顾目标

<table border="2" style="border-collapse: collapse;">
    <tr>
       <th>项目需求来源</th>
       <td>2021 年 7 月 16 日开展珠海市农村电商“一村一品”为期三个月的课程培训</td>
    </tr>
    <tr>
        <th>项目价值</th>
        <td>没有需求说明，盲猜是为了给平台增加用户流量，以及政府合作</td>
    </tr>
    <tr>
        <th>项目目标</th>
        <td>没有需求说明，从探索系统可知主流程是上传用户报名信息，用户可参加课程打卡</td>
    </tr>
    <tr>
        <th rowspan="3">预先设定的项目计划（重要里程碑）</th>
        <td>1. 用户可以正常使用小程序的功能</td>
    </tr>
    <tr>
        <td>2. 运营人员可以正常使用后台管理系统对前台的数据进行核检</td>
    </tr>
    <tr>
        <td>3. 小程序端的签到打卡接口在达到 200 个 vus 时服务无异常</td>
    </tr>
    <tr>
        <th rowspan="8">预先设想的项目风险</th>
        <td>1. 不熟悉业务流程的用户可能导致请求失败或请求异常</td>
    </tr>
    <tr>
        <td>2. 由于小程序存在手机系统兼容性问题，导致部分用户无法正常操作</td>
    </tr>
    <tr>
        <td>3. 由于未对小程序的权限问题进行针对性测试，导致部分用户授权失败</td>
    </tr>
    <tr>
        <td>4. 小程序的更新需要发版上线，在体验版测试通过后更新到正式版的中间存在审核时间，导致已解决的问题无法及时更新到正式版</td>
    </tr>
    <tr>
        <td>5. 由于项目测试时间紧凑，测试不充分，导致功能测试范围覆盖率不够高</td>
    </tr>
    <tr>
        <td>6. 由于前期没有详细的需求说明文档，导致项目组成员对需求的理解不一致</td>
    </tr>
    <tr>
        <td>7. 仅通过基础的功能性验证就发版上线，未考虑非功能性验证，导致用户体验效果极差</td>
    </tr>
    <tr>
        <td>8. 正式版一上线后就大量删除测试数据，由于测试数据不充足，导致前端页面测试不充分</td>
    </tr>
</table>

<br><br>


## 三、评估结果

<table border="2" style="border-collapse: collapse;">
    <tr>
        <th>实际项目情况（是否出现事故，没有写无）</th>
        <td>项目在上线后出现事故</td>
    </tr>
    <tr>
        <th rowspan="7">突发事故是在什么情况下发生的？</th>
        <td>1. 缺乏操作引导，导致用户在不熟悉业务流程的条件下签到打卡失败</td>
    </tr>
    <tr>
        <td>2. 缺乏对接口提示信息的校验，非正确性操作时接口均提示“未知异常，请联系管理员”，导致让用户误以为系统异常，影响体验</td>
    </tr>
    <tr>
        <td>3. 当前项目使用 session 来保持会话，由于前后端未明确 session 处理，导致前台用户的身份信息时不时发生互窜，即用户A的个人页显示用户B的昵称和头像等信息</td>
    </tr>
    <tr>
        <td>4. 由于网络问题，导致用户授权失败，但是前端遇到网络问题未做提示，导致用户体验极差</td>
    </tr>
    <tr>
        <td>5. 后面新增了审核通过后生成学员编号功能，审核通过后，前台的用户个人页未刷新学员编号的值，重新进入小程序才显示学员编号</td>
    </tr>
    <tr>
        <td>6. 用户的 session 过期后，在小程序的个人页点击个人头像后弹出的微信授权框未显示授权按钮</td>
    </tr>
    <tr>
        <td>7. 小程序修复的问题需要发布到正式版，但是由于存在审核，导致已修复的问题无法快速更新</td>
    </tr>
    <tr>
        <th>对比目标，是否有超额完成事件？没有就写无</th>
        <td>时间短，仅有三天测试时间，在此期间内需要测试接口、小程序、后台系统，已保证正常流程的走通，已无更多时间覆盖异常场景</td>
    </tr>
    <tr>
        <th rowspan="3">哪些地方未达到预期？</th>
        <td>1. 用户身份认证测试不充分</td>
    </tr>
    <tr>
        <td>2. 用户打卡场景测试不充分</td>
    </tr>
    <tr>
        <td>3. 用户授权场景测试不充分</td>
    </tr>
</table>

<br><br>


## 四、分析原因

<table border="2" style="border-collapse: collapse;">
    <tr>
        <th>实际结果与预期结果有无差异</th>
        <td>有很大的差异</td>
    </tr>
    <tr>
        <th rowspan="4">产生差异的客观原因</th>
        <td>1. 时间不给力</td>
    </tr>
    <tr>
        <td>2. 需求变动大</td>
    </tr>
    <tr>
        <td>3. 后台改动多</td>
    </tr>
    <tr>
        <td>4. 人手不够</td>
    </tr>
    <tr>
        <th rowspan="3">产生差异的主观原因</th>
        <td>1. 需求不清晰，都在摸石头过河</td>
    </tr>
    <tr>
        <td>2. 前后台新增功能未提醒测试人员，导致漏测</td>
    </tr>
    <tr>
        <td>3. 小程序非功能性测试场景缺乏</td>
    </tr>
    <tr>
        <th rowspan="5">可借鉴经验</th>
        <td>1. 根据用户打卡场景分析，可以设计一个负载测试策略，vus 从 60 开始热身，逐渐增加到 200 后恢复</td>
    </tr>
    <tr>
        <td>2. 从网络状态下手，遇到网络差的情况前端需提示</td>
    </tr>
    <tr>
        <td>3. 我觉得运营人员首先自己要很了解这个业务流程，然后再设计一个大的海报去引导用户操作，而不是去让用户试错</td>
    </tr>
    <tr>
        <td>4. 活动现场可以安排一个技术人员，有异常可以先快速排查，而不是远程协助，这样效率很低</td>
    </tr>
    <tr>
        <td>5. 经过这次教训，我发现不同的提示信息都需要传达准确度，要让用户感知到发生了什么事导致的，而不是让用户去猜，这样体验很差</td>
    </tr>
</table>

<br><br>


## 五、总结经验（项目中学到的新事物）

<table border="2" style="border-collapse: collapse;">
    <tr>
        <th rowspan="2">产品设计方面</th>
        <td>1. 流程清晰，一目了然</td>
    </tr>
    <tr>
        <td>2. 不同的活动对应不同的主题版面</td>
    </tr>
    <tr>
        <th rowspan="5">产品研发方面</th>
        <td>1. 很多公司在会话机制上都使用了 token，只有我们的项目还在用 session，所以今后需要进行 session 测试</td>
    </tr>
    <tr>
        <td>2. 小程序需要进行授权测试</td>
    </tr>
    <tr>
        <td>3. 小程序需要进行网络测试</td>
    </tr>
    <tr>
        <td>4. 小程序需要进行性能测试</td>
    </tr>
    <tr>
        <td>5. 小程序需要进行兼容测试</td>
    </tr>
    <tr>
        <th rowspan="2">项目管理方面</th>
        <td>1. 我真的觉得领导存在的意义就是为下属争取上线的时间，而不是跟个扯线木偶一样，别人说啥就是啥</td>
    </tr>
    <tr>
        <td>2. 需求文档真的是硬伤，这次干脆都没有需求设计说明，啥都靠自己脑补，摸石头过河</td>
    </tr>
</table>