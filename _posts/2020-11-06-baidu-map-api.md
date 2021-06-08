---
layout: post
title: "百度 API | 百度地图添加标注的 js 代码"
subtitle: "看看自动生成的代码，然后根据 api 进行组装和删减"
author: "Haauleon"
header-style: text
tags:
  - 百度 API
---


## 实现效果
![](\img\in-post\post-other\2020-11-06-baidu-map-api-1.jpg) 
<br>

## 完整的 html 代码
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>百度地图API自定义地图</title>
<!--引用百度地图API-->
<style type="text/css">
    html,body{margin:0;padding:0;}
    .iw_poi_title {color:#CC5522;font-size:14px;font-weight:bold;overflow:hidden;padding-right:13px;white-space:nowrap}
    .iw_poi_content {font:12px arial,sans-serif;overflow:visible;padding-top:4px;white-space:-moz-pre-wrap;word-wrap:break-word}
</style>
<script type="text/javascript" src="http://api.map.baidu.com/api?key=&v=1.1&services=true"></script>
</head>

<body>
  <!--百度地图容器-->
  <div style="width:697px;height:550px;border:#ccc solid 1px;" id="dituContent"></div>
</body>
<script type="text/javascript">
    //创建和初始化地图函数：
    function initMap(){
        createMap();//创建地图
        setMapEvent();//设置地图事件
        addMapControl();//向地图添加控件
        addMarker();//向地图中添加marker
    }
    
    //创建地图函数：
    function createMap(){
        var map = new BMap.Map("dituContent");//在百度地图容器中创建一个地图
        var point = new BMap.Point(113.549937,22.137441);//定义一个中心点坐标
        map.centerAndZoom(point,17);//设定地图的中心点和坐标并将地图显示在地图容器中
        window.map = map;//将map变量存储在全局
    }
    
    //地图事件设置函数：
    function setMapEvent(){
        map.enableDragging();//启用地图拖拽事件，默认启用(可不写)
        map.enableScrollWheelZoom();//启用地图滚轮放大缩小
        map.enableDoubleClickZoom();//启用鼠标双击放大，默认启用(可不写)
        map.enableKeyboard();//启用键盘上下左右键移动地图
    }
    
    //地图控件添加函数：
    function addMapControl(){
        //向地图中添加缩放控件
	var ctrl_nav = new BMap.NavigationControl({anchor:BMAP_ANCHOR_TOP_LEFT,type:BMAP_NAVIGATION_CONTROL_LARGE});
	map.addControl(ctrl_nav);
        //向地图中添加比例尺控件
	var ctrl_sca = new BMap.ScaleControl({anchor:BMAP_ANCHOR_BOTTOM_LEFT});
	map.addControl(ctrl_sca);
    }
    
    //标注点数组
    var markerArr = [{title:"我的标记",content:"我的备注",point:"113.548814|22.138529",isOpen:1,icon:{w:21,h:21,l:0,t:0,x:6,lb:5}}
		 ];
    //创建标注覆盖物
    function addMarker(){
        for(var i=0;i<markerArr.length;i++){ // 遍历标注点数组
            var json = markerArr[i]; // 定义变量指向标注点数组的每一个标注
            var p0 = json.point.split("|")[0]; // 获取每一个标注的x轴坐标
            var p1 = json.point.split("|")[1]; // 获取每一个标注的y轴坐标
            var point = new BMap.Point(p0,p1); // 实例化一个坐标点(x, y)对象
			var iconImg = createIcon(json.icon); // 创建一个坐标点对应的 Icon
            var marker = new BMap.Marker(point,{icon:iconImg}); // 创建一个图像标注实例。point参数指定了图像标注所在的地理位置
            map.addOverlay(marker); // 全景场景内添加覆盖物
        }
    }

    //创建一个Icon
    function createIcon(json){ // Size 以指定的宽度和高度创建一个矩形区域大小对象
        // Icon 以给定的图像地址和大小创建图标对象实例
        var icon = new BMap.Icon("http://api.map.baidu.com/lbsapi/creatmap/images/us_mk_icon.png", new BMap.Size(json.w,json.h),{imageOffset: new BMap.Size(-json.l,-json.t),infoWindowOffset:new BMap.Size(json.lb+5,1),offset:new BMap.Size(json.x,json.h)})
        return icon;
    }
    
    initMap();//创建和初始化地图
</script>
</html>
```