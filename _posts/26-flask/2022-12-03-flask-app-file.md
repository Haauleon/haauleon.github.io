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
werkzeug==0.11.10       

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
&emsp;&emsp;文件中只包含了 PasteFile 模型，字段定义和初始化方法如下：     
```python
# coding=utf-8
"""
@File    :   models.py
@Function:   存放模型
"""
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
        """文件名加密"""
        _, _, suffix = filename.rpartition('.')
        return '%s.%s' % (uuid.uuid4().hex, suffix)
```  

<br>
<br>

#### 7、app.py    
&emsp;&emsp;使用 SharedDataMiddleware 是实现在页面读取源文件的最简单的方法。      

&emsp;&emsp;如下代码片段，只是把第三方扩展初始化放在了 app.py 文件中，而没有使用 `db = SQLAlchemy(app)` 这样的方法。这是因为在大型应用中如果 db 被多个模型文件引用的话，会造成 `from app import db` 这样的方式，但是往往在 app.py 中也会引用模型文件定义的类，这样就造成了循环引用。所以最好的方式是把它放在不依赖其他模块的独立文件中。   
```python
# coding=utf-8
"""
@File    :   app.py
@Function:   应用主程序
"""
import os

from werkzeug import SharedDataMiddleware
from flask import abort, Flask, request, jsonify, redirect, send_file

from ext import db, mako, render_template
from models import PasteFile
from utils import get_file_path, humanize_bytes

ONE_MONTH = 60 * 60 * 24 * 30

app = Flask(__name__, template_folder='../../templates/r',
            static_folder='../../static')
app.config.from_object('config')

app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/i/': get_file_path()
})

mako.init_app(app)
db.init_app(app)
```

<br>
<br>

#### 8、requirements.txt
&emsp;&emsp;项目依赖的第三方 pip 包集合文件，可以使用命令行 `> pip install -r requirements.txt` 进行批量安装。      
```python
python-magic==0.4.10
Pillow==3.2.0
cropresize2==0.1.9
short-url==1.2.1
```

<br>
<br>

### 四、视图实现
&emsp;&emsp;以下分别是首页、重置设置图片页、下载页、预览页和短链接页的视图及其实现逻辑。   

<br>

#### 1、首页
&emsp;&emsp;首页就是上传图片页，通过这个页面可以上传图片，并生成预览页：    
```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        """如果是POST请求则通过 PasteFile.create_by_upload_file 创建一个 paste_file 实例"""
        uploaded_file = request.files['file']
        w = request.form.get('w')
        h = request.form.get('h')
        if not uploaded_file:
            return abort(400)

        if w and h:
            """如果传入的图片长和宽不为空，则按照指定的长宽进行图片裁剪并保存"""
            paste_file = PasteFile.rsize(uploaded_file, w, h)
        else:
            """否则保存上传的图片"""
            paste_file = PasteFile.create_by_upload_file(uploaded_file)
        db.session.add(paste_file)
        db.session.commit()

        return jsonify({
            'url_d': paste_file.url_d,
            'url_i': paste_file.url_i,
            'url_s': paste_file.url_s,
            'url_p': paste_file.url_p,
            'filename': paste_file.filename,
            'size': humanize_bytes(paste_file.size),
            'time': str(paste_file.uploadtime),
            'type': paste_file.type,
            'quoteurl': paste_file.quoteurl
        })
    """如果是GET请求则直接渲染 index.html"""
    return render_template('index.html', **locals())
```

```python
...

class PasteFile(db.Model):
    ...

    @property
    def path(self):
        # 为了防止不同的用户上传了同名文件造成文件的替换问题，使用了随机命名 filehash
        return get_file_path(self.filehash)

    @classmethod
    def get_by_md5(cls, filemd5):
        return cls.query.filter_by(filemd5=filemd5).first()

    @classmethod
    def create_by_upload_file(cls, uploaded_file):
        """
        创建文件
        @param uploaded_file:
        @return:
        """
        rst = cls(uploaded_file.filename, uploaded_file.mimetype, 0)
        # 创建 PasteFile 实例前会先保存文件，保存的文件名是 rst.path
        uploaded_file.save(rst.path)
        with open(rst.path, 'rb') as f:
            # 通过文件的 md5 值判断该文件之前是否已经上传过，如果是就直接删掉刚保存的文件 rst.path 并返回之前创建的文件
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
    def rsize(cls, old_paste, weight, height):
        """
        根据指定的长和宽裁剪图片并保存
        @param old_paste: 旧图片
        @param weight: 长
        @param height: 宽
        @return:
        """
        assert old_paste.is_image, TypeError('Unsupported Image Type.')
        f = open(old_paste.path, 'rb')
        im = Image.open(f)

        img = cropresize2.crop_resize(im, (int(weight), int(height)))

        rst = cls(old_paste.filename, old_paste.mimetype, 0)
        img.save(rst.path)
        filestat = os.stat(rst.path)
        rst.size = filestat.st_size
        return rst
```
<br>
<br>

#### 2、重置设置图片页
&emsp;&emsp;支持对现有的图片重新设置大小，返回新的图片地址：     
```python
@app.route('/r/<img_hash>')
def rsize(img_hash):
    w = request.args['w']
    h = request.args['h']

    old_paste = PasteFile.get_by_filehash(img_hash)
    new_paste = PasteFile.rsize(old_paste, w, h)

    return new_paste.url_i
```

```python
class PasteFile(db.Model):
    ...

    @classmethod
    def get_by_filehash(cls, filehash, code=404):
        """
        从数据库中找到匹配 filehash 的条目
        @param filehash:
        @param code:
        @return:
        """
        return cls.query.filter_by(filehash=filehash).first() or abort(code)

    def get_url(self, subtype, is_symlink=False):
        """
        通过 get_url 可以拼不同类型的请求地址
        @param subtype:
        @param is_symlink:
        @return:
        """
        hash_or_link = self.symlink if is_symlink else self.filehash
        return 'http://{host}/{subtype}/{hash_or_link}'.format(
            subtype=subtype, host=request.host, hash_or_link=hash_or_link)

    @property
    def url_i(self):
        """
        获取源文件的地址
        @return:
        """
        return self.get_url('i')

    @property
    def url_p(self):
        """
        获取文件预览地址
        @return:
        """
        return self.get_url('p')

    @property
    def url_s(self):
        """
        获取文件短链接地址
        @return:
        """
        return self.get_url('s', is_symlink=True)

    @property
    def url_d(self):
        """
        获取文件下载地址
        @return:
        """
        return self.get_url('d')
```

<br>
<br>

#### 3、下载页
&emsp;&emsp;下载文件时使用 `/d/img_hash.jpg` 这样的地址，可以用 Flask 提供的 send_file 实现：    
```python
from flask import send_file

ONE_MONTH = 60 * 60 * 24 * 30


@app.route('/d/<filehash>', methods=['GET'])
def download(filehash):
    paste_file = PasteFile.get_by_filehash(filehash)

    return send_file(open(paste_file.path, 'rb'),
                     mimetype='application/octet-stream',
                     cache_timeout=ONE_MONTH,
                     as_attachment=True,
                     attachment_filename=paste_file.filename.encode('utf-8'))
```

<br>
<br>

#### 4、预览页
&emsp;&emsp;预览文件使用 `/p/img_hash.jpg` 这样的地址。在首页上传完毕时也会在地址栏显示了这样的地址，但事实上并没有发生跳转，只是用了 JavaScript 修改了地址。由于它们使用了同一个文件卡片组件，所以看起来一模一样。           
```python
@app.route('/p/<filehash>')
def preview(filehash):
    paste_file = PasteFile.get_by_filehash(filehash)

    if not paste_file:
        filepath = get_file_path(filehash)
        if not(os.path.exists(filepath) and (not os.path.islink(filepath))):
            return abort(404)

        paste_file = PasteFile.create_by_old_paste(filehash)
        db.session.add(paste_file)
        db.session.commit()

    return render_template('success.html', p=paste_file)
```

<br>
<br>

#### 5、短链接页
&emsp;&emsp;由于 hash 值太长，支持使用短链接的方式访问，使用 `/s/short_url` 这样的地址。但是并不需要把短链接存放进数据库，正确的做法是用 id 这个唯一标识生成短链接地址。         
```python
@app.route('/s/<symlink>')
def s(symlink):
    paste_file = PasteFile.get_by_symlink(symlink)

    return redirect(paste_file.url_p)
```

```python
class PasteFile(db.Model):
    ...

    @cached_property
    def symlink(self):
        return short_url.encode_url(self.id)

    @classmethod
    def get_by_symlink(cls, symlink, code=404):
        """通过短链接获得对应数据库条目的方法"""
        id = short_url.decode_url(symlink)
        return cls.query.filter_by(id=id).first() or abort(code)
```