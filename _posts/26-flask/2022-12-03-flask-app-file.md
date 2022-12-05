---
layout:        post
title:         "Flask Web | 文件托管服务"
subtitle:      "实现一个文件托管服务"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、需求列表
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

文件托管服务的需求说明如下：     
1. 上传后的文件可以被永久存放。    
2. 上传后的文件有一个功能完备的预览页。预览页显示文件大小、文件类型、上传时间、下载地址和短链接等信息。     
3. 可以通过传参数对图片进行缩放和剪切。    
4. 不错的页面展示效果。    
5. 为节省空间，相同文件不重复上传，如果文件已经上传过，则直接返回之前上传的文件。    

<br>
<br>

### 二、项目准备
#### 1、环境准备
先安装一些依赖：    
```
> sudo apt-get install libjpeg8-dev -yq
> sudo pip install -r requirements.txt
```

requirements.txt 的 pip 第三方包列表如下：    
```python
python-magic==0.4.10  # libmagic 的 Python 绑定，用于确定文件类型 
Pillow==3.2.0         # PIL(Python Imaging Library) 的分支，用来替代 PIL 
cropresize2==0.1.9    # 用来剪切和调整图片大小
short-url==1.2.1      # 创建短链接
```

<br>

#### 2、建表语句
文件托管服务的建表语句如下:          
```sql
CREATE TABLE `PasteFile` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `filename` varchar(5000) NOT NULL,
    `filehash` varchar(128) NOT NULL,
    `filemd5` varchar(128) NOT NULL,
    `uploadtime` datetime NOT NULL,
    `mimetype` varchar(256) NOT NULL,
    `size` int(11) unsigned NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `filehash` (`filehash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

&emsp;&emsp;建表时指定了 `ENGINE=InnoDB`，意味着这个表会使用 InnoDB 引擎，这是 MySQL 的默认存储引擎。现在创建一个文件 databases/schema.sql，写入以上建表 SQL 语句，然后使用命令行将该文件导入到数据库中：            
```
❯ vim databases/schema.sql
> (echo "use r"; cat databases/schema.sql) | mysql --user='web' --password='web'
```

&emsp;&emsp;将表导入到数据库后，可以通过以下命令检查是否导入成功：    
```
> sudo mysql -u root
mysql> use r;
mysql> DESC PasteFile;
+------------+------------------+------+-----+---------+----------------+
| Field      | Type             | Null | Key | Default | Extra          |
+------------+------------------+------+-----+---------+----------------+
| id         | int(11)          | NO   | PRI | NULL    | auto_increment |
| filename   | varchar(5000)    | NO   |     | NULL    |                |
| filehash   | varchar(128)     | NO   |     | NULL    |                |
| filemd5    | varchar(128)     | NO   |     | NULL    |                |
| uploadtime | datetime         | NO   |     | NULL    |                |
| mimetype   | varchar(256)     | NO   |     | NULL    |                |
| size       | int(11) unsigned | NO   |     | NULL    |                |
+------------+------------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)
```

<br>
<br>

### 三、项目结构
```
 ❯ tree web
web
├── __init__.py
├── config.py         # 用于存放配置
├── utils.py          # 用于存放功能函数
├── mimes.py          # 只接受文件中定义了的媒体类型
├── ext.py            # 存放扩展的封装
├── models.py         # 存放模型
├── app.py            # 存放主程序
└── requirements.txt  # 项目依赖集合文件

0 directories, 8 files
```

<br>

#### 1、__init__.py     
&emsp;&emsp;`__init__.py` 会在 import 的时候被执行，而空的 `__init__.py` 在 Python 新版本（Python3.8 版本）中已经不需要你额外去定义了，因为就算你不定义 init， Python 也知道你导入的包路径。但如果想做一些初始化操作或者预先导入相关的模块，那么定义 `__init__.py` 还是很有必要的。     

&emsp;&emsp;该项目仍使用的是 python 2.7.11+，需要定义一个 `__init__.py` 文件，此文件为空文件。    

<br>
<br>

#### 2、config.py     
```python
# coding=utf-8
"""
@File    :   config.py
@Function:   用于存放配置
"""
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://web:web@localhost:3306/r'
# 指定存放上传文件的目录
UPLOAD_FOLDER = '/tmp/permdir'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

<br>
<br>

#### 3、utils.py      
```python
# coding=utf-8
"""
@File    :   utils.py
@Function:   用于存放功能函数
"""
import os
import hashlib
from functools import partial

from config import UPLOAD_FOLDER

HERE = os.path.abspath(os.path.dirname(__file__))


def get_file_md5(f, chunk_size=8192):
    """
    获得文件的 md5 值
    @param f:
    @param chunk_size:
    @return:
    """
    h = hashlib.md5()
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        h.update(chunk)
    return h.hexdigest()


def humanize_bytes(bytesize, precision=2):
    """
    返回可读的文件大小
    @param bytesize:
    @param precision: 保留小数点后多少位，默认是精确到后两位
    @return:
    """
    abbrevs = (
        (1 << 50, 'PB'),  # 1 << 50 == 2^50 == 1125899906842624 bytes == 1PB
        (1 << 40, 'TB'),  # 1 << 40 == 2^40 == 1099511627776 bytes == 1TB
        (1 << 30, 'GB'),  # 1 << 30 == 2^30 == 1073741824 bytes == 1GB
        (1 << 20, 'MB'),  # 1 << 20 == 2^20 == 1048576 bytes == 1MB
        (1 << 10, 'kB'),  # 1 << 10 == 2^10 == 1024 bytes == 1KB
        (1, 'bytes')
    )
    if bytesize == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytesize >= factor:
            break
    return '%.*f %s' % (precision, bytesize / factor, suffix)


get_file_path = partial(os.path.join, HERE, UPLOAD_FOLDER)
```

<br>
<br>

#### 4、mimes.py     
```python
# coding=utf-8
"""
@File    :   mimes.py
@Function:   只接受文件中定义了的媒体类型
"""
AUDIO_MIMES = [
    'audio/x-aac',
    'audio/mp4',
    'audio/ogg',
    'audio/mpeg',
    'audio/x-m4a',
    'audio/mp3'
]

IMAGE_MIMES = [
    'image/x-icon',
    'image/svg+xml',
    'image/jpeg',
    'image/gif',
    'image/png',
    'image/webp'
]

VIDEO_MIMES = [
    'video/x-msvideo',
    'video/quicktime',
    'video/mpeg',
    'video/h264',
    'video/mp4',
    'video/ogg',
    'video/webm',
]
```

<br>
<br>

#### 5、ext.py       
```python
# coding=utf-8
"""
@File    :   ext.py
@Function:   存放扩展的封装
"""
from flask_mako import MakoTemplates, render_template  # noqa
from flask_sqlalchemy import SQLAlchemy

mako = MakoTemplates()
db = SQLAlchemy()
```

<br>
<br>

#### 6、models.py    
&emsp;&emsp;文件中只包含了 PasteFile 模型  
```python
# coding=utf-8
"""
@File    :   models.py
@Function:   存放模型
"""
import os
import uuid
import magic
from datetime import datetime

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

import cropresize2
import short_url
from PIL import Image
from flask import abort, request
from werkzeug.utils import cached_property

from mimes import IMAGE_MIMES, AUDIO_MIMES, VIDEO_MIMES
from utils import get_file_md5, get_file_path
from ext import db


class PasteFile(db.Model):
    __tablename__ = 'PasteFile'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(5000), nullable=False)
    filehash = db.Column(db.String(128), nullable=False, unique=True)
    filemd5 = db.Column(db.String(128), nullable=False, unique=True)
    uploadtime = db.Column(db.DateTime, nullable=False)
    mimetype = db.Column(db.String(256), nullable=False)
    size = db.Column(db.Integer, nullable=False)

    def __init__(self, filename='', mimetype='application/octet-stream',
                 size=0, filehash=None, filemd5=None):
        self.uploadtime = datetime.now()
        self.mimetype = mimetype
        self.size = int(size)
        self.filehash = filehash if filehash else self._hash_filename(filename)
        self.filename = filename if filename else self.filehash
        self.filemd5 = filemd5

    @staticmethod
    def _hash_filename(filename):
        _, _, suffix = filename.rpartition('.')
        return '%s.%s' % (uuid.uuid4().hex, suffix)

    @cached_property
    def symlink(self):
        return short_url.encode_url(self.id)

    @classmethod
    def get_by_symlink(cls, symlink, code=404):
        id = short_url.decode_url(symlink)
        return cls.query.filter_by(id=id).first() or abort(code)

    @classmethod
    def get_by_filehash(cls, filehash, code=404):
        return cls.query.filter_by(filehash=filehash).first() or abort(code)

    @classmethod
    def get_by_md5(cls, filemd5):
        return cls.query.filter_by(filemd5=filemd5).first()

    @classmethod
    def create_by_upload_file(cls, uploaded_file):
        rst = cls(uploaded_file.filename, uploaded_file.mimetype, 0)
        uploaded_file.save(rst.path)
        with open(rst.path, 'rb') as f:
            filemd5 = get_file_md5(f)
            uploaded_file = cls.get_by_md5(filemd5)
            if uploaded_file:
                os.remove(rst.path)
                return uploaded_file
        filestat = os.stat(rst.path)
        rst.size = filestat.st_size
        rst.filemd5 = filemd5
        return rst

    @classmethod
    def create_by_old_paste(cls, filehash):
        filepath = get_file_path(filehash)
        mimetype = magic.from_file(filepath, mime=True)
        filestat = os.stat(filepath)
        size = filestat.st_size

        rst = cls(filehash, mimetype, size, filehash=filehash)
        return rst

    @property
    def path(self):
        return get_file_path(self.filehash)

    def get_url(self, subtype, is_symlink=False):
        hash_or_link = self.symlink if is_symlink else self.filehash
        return 'http://{host}/{subtype}/{hash_or_link}'.format(
            subtype=subtype, host=request.host, hash_or_link=hash_or_link)

    @property
    def url_i(self):
        return self.get_url('i')

    @property
    def url_p(self):
        return self.get_url('p')

    @property
    def url_s(self):
        return self.get_url('s', is_symlink=True)

    @property
    def url_d(self):
        return self.get_url('d')

    @property
    def image_size(self):
        if self.is_image:
            f = open(self.path, 'rb')
            im = Image.open(f)
            return im.size
        return (0, 0)

    @property
    def quoteurl(self):
        return quote(self.url_i)

    @classmethod
    def rsize(cls, old_paste, weight, height):
        assert old_paste.is_image, TypeError('Unsupported Image Type.')
        f = open(old_paste.path, 'rb')
        im = Image.open(f)

        img = cropresize2.crop_resize(im, (int(weight), int(height)))

        rst = cls(old_paste.filename, old_paste.mimetype, 0)
        img.save(rst.path)
        filestat = os.stat(rst.path)
        rst.size = filestat.st_size
        return rst

    @property
    def is_image(self):
        return self.mimetype in IMAGE_MIMES

    @property
    def is_audio(self):
        return self.mimetype in AUDIO_MIMES

    @property
    def is_video(self):
        return self.mimetype in VIDEO_MIMES

    @property
    def is_pdf(self):
        return self.mimetype == 'application/pdf'

    @property
    def type(self):
        for t in ('image', 'pdf', 'video', 'audio'):
            if getattr(self, 'is_' + t):
                return t
        return 'binary'
```

<br>
<br>

#### 7、app.py    


<br>
<br>

#### 8、requirements.txt
```python
python-magic==0.4.10
Pillow==3.2.0
cropresize2==0.1.9
short-url==1.2.1
```

<br>
<br>