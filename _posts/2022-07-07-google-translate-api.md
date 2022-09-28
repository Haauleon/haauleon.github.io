---
layout:        post
title:         "谷歌 | 免费的 google 翻译 api"
subtitle:      "有一些异常需要处理"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 小而美脚本
---

> 参考 https://blog.csdn.net/linweidong/article/details/113866543

<br><br>

### 背景
&emsp;&emsp;他们说百度翻译不够地道，然后我就找到了官方的谷歌翻译，一看是收费的就放弃了，后来功夫不负有心人还是找到一个可用的且免费的 google 翻译 api。   

<br><br>

### 开源项目
项目地址：[https://github.com/Saravananslb/py-googletranslation](https://github.com/Saravananslb/py-googletranslation)        

&emsp;&emsp;这个开源项目要求依赖是  Python 3.6+ ，为了使用方便，安装了带 pip 管理工具下载 py-googletranslation。    
```
$ pip install pygoogletranslation==2.0.3
```

<br>

&emsp;&emsp;原来开源项目默认的 google.com 是访问不了的，要做下面修改，或直接找到下载代码，把 google.com 修改为 google.cn 。        
```python
>>> from googletrans import Translator
>>> translator = Translator(service_urls=[
      'translate.google.cn',   
    ])
```

<br>

**基础用法：**    
如果没有指定源语言，会自动侦测源语言      
```python
>>> from pygoogletranslation import Translator
>>> translator = Translator()
>>> translator.translate('Good Morning', dest='ta')
# <Translated src=ko dest=ta text=காலை வணக்கம். pronunciation=Good evening.>
>>> translator.translate('안녕하세요.', dest='ja')
# <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
>>> translator.translate('veritas lux mea', src='la')
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
```

<br>

**高级用法（批量）：**           
可以使用数组批量翻译，只是简单调用一个 http session     
```
>>> from pygoogletranslation import Translator
>>> translator = Translator()
>>> t = (translator.translate(["Good ' Morning", "India"], dest="ta"))
>>> for _t in t:
>>>     print(_t.text)
# காலை வணக்கம்
# இந்தியா
```

<br>

**语言检测：**     
```python
>>> from pygoogletranslation import Translator
>>> translator = Translator()
>>> translator.detect('காலை வணக்கம்,')
# <Detected lang=ta confidence=0.72041003>
>>> translator.detect('この文章は日本語で書かれました。')
# <Detected lang=ja confidence=0.64889508>
>>> translator.detect('This sentence is written in English.')
# <Detected lang=en confidence=0.22348526>
>>> translator.detect('Tiu frazo estas skribita en Esperanto.')
# <Detected lang=eo confidence=0.10538048>
```

<br>

**翻译文档类型的（.doc, .docx, .pdf, .txt）：**        
```python
>>> from pygoogletranslation import Translator
>>> translator = Translator()
>>> translator.bulktranslate('test.txt', dest="ta")
# <bulk translated text>
# for bulk translation, sometimes you might get an error with response
# code "429" - Too Many attempts.
# To overcome this error, add below parameter.
>>> translator = Translator(retry=NO_OF_ATTEMPTS, sleep=WAIT_SECONDS, retry_message=TRUE)
>>> translator.bulktranslate('test.txt', dest="ta")
# retry - no of attemps (default- 3 times)
# sleep - no of attempts after seconds (default- 5 seconds)
# retry_message - True - display retrying message (default- False)
```

<br>

**pygoogletranslation 定义的语言列表**    
```python
>>> from pygoogletranslation import Translator
>>> translator = Translator()
>>> translator.glanguage()
>>> {
   "sl": {
   "auto": "Detect language",
   "af": "Afrikaans",
   "sq": "Albanian",
   "am": "Amharic",
   "ar": "Arabic",
   "hy": "Armenian",
   "az": "Azerbaijani",
   "eu": "Basque",
   "be": "Belarusian",
   "bn": "Bengali",
   "bs": "Bosnian",
   "bg": "Bulgarian",
   "ca": "Catalan",
   "ceb": "Cebuano",
   "ny": "Chichewa",
   "zh-CN": "Chinese",
   "co": "Corsican",
   "hr": "Croatian",
   "cs": "Czech",
   "da": "Danish",
   "nl": "Dutch",
   "en": "English",
   "eo": "Esperanto",
   "et": "Estonian",
   "tl": "Filipino",
   "fi": "Finnish",
   "fr": "French",
   "fy": "Frisian",
   "gl": "Galician",
   "ka": "Georgian",
   "de": "German",
   "el": "Greek",
   "gu": "Gujarati",
   "ht": "Haitian Creole",
   "ha": "Hausa",
   "haw": "Hawaiian",
   "iw": "Hebrew",
   "hi": "Hindi",
   "hmn": "Hmong",
   "hu": "Hungarian",
   "is": "Icelandic",
   "ig": "Igbo",
   "id": "Indonesian",
   "ga": "Irish",
   "it": "Italian",
   "ja": "Japanese",
   "jw": "Javanese",
   "kn": "Kannada",
   "kk": "Kazakh",
   "km": "Khmer",
   "rw": "Kinyarwanda",
   "ko": "Korean",
   "ku": "Kurdish (Kurmanji)",
   "ky": "Kyrgyz",
   "lo": "Lao",
   "la": "Latin",
   "lv": "Latvian",
   "lt": "Lithuanian",
   "lb": "Luxembourgish",
   "mk": "Macedonian",
   "mg": "Malagasy",
   "ms": "Malay",
   "ml": "Malayalam",
   "mt": "Maltese",
   "mi": "Maori",
   "mr": "Marathi",
   "mn": "Mongolian",
   "my": "Myanmar (Burmese)",
   "ne": "Nepali",
   "no": "Norwegian",
   "or": "Odia (Oriya)",
   "ps": "Pashto",
   "fa": "Persian",
   "pl": "Polish",
   "pt": "Portuguese",
   "pa": "Punjabi",
   "ro": "Romanian",
   "ru": "Russian",
   "sm": "Samoan",
   "gd": "Scots Gaelic",
   "sr": "Serbian",
   "st": "Sesotho",
   "sn": "Shona",
   "sd": "Sindhi",
   "si": "Sinhala",
   "sk": "Slovak",
   "sl": "Slovenian",
   "so": "Somali",
   "es": "Spanish",
   "su": "Sundanese",
   "sw": "Swahili",
   "sv": "Swedish",
   "tg": "Tajik",
   "ta": "Tamil",
   "tt": "Tatar",
   "te": "Telugu",
   "th": "Thai",
   "tr": "Turkish",
   "tk": "Turkmen",
   "uk": "Ukrainian",
   "ur": "Urdu",
   "ug": "Uyghur",
   "uz": "Uzbek",
   "vi": "Vietnamese",
   "cy": "Welsh",
   "xh": "Xhosa",
   "yi": "Yiddish",
   "yo": "Yoruba",
   "zu": "Zulu"
   },
   "tl": {
   "af": "Afrikaans",
   "sq": "Albanian",
   "am": "Amharic",
   "ar": "Arabic",
   "hy": "Armenian",
   "az": "Azerbaijani",
   "eu": "Basque",
   "be": "Belarusian",
   "bn": "Bengali",
   "bs": "Bosnian",
   "bg": "Bulgarian",
   "ca": "Catalan",
   "ceb": "Cebuano",
   "ny": "Chichewa",
   "zh-CN": "Chinese (Simplified)",
   "zh-TW": "Chinese (Traditional)",
   "co": "Corsican",
   "hr": "Croatian",
   "cs": "Czech",
   "da": "Danish",
   "nl": "Dutch",
   "en": "English",
   "eo": "Esperanto",
   "et": "Estonian",
   "tl": "Filipino",
   "fi": "Finnish",
   "fr": "French",
   "fy": "Frisian",
   "gl": "Galician",
   "ka": "Georgian",
   "de": "German",
   "el": "Greek",
   "gu": "Gujarati",
   "ht": "Haitian Creole",
   "ha": "Hausa",
   "haw": "Hawaiian",
   "iw": "Hebrew",
   "hi": "Hindi",
   "hmn": "Hmong",
   "hu": "Hungarian",
   "is": "Icelandic",
   "ig": "Igbo",
   "id": "Indonesian",
   "ga": "Irish",
   "it": "Italian",
   "ja": "Japanese",
   "jw": "Javanese",
   "kn": "Kannada",
   "kk": "Kazakh",
   "km": "Khmer",
   "rw": "Kinyarwanda",
   "ko": "Korean",
   "ku": "Kurdish (Kurmanji)",
   "ky": "Kyrgyz",
   "lo": "Lao",
   "la": "Latin",
   "lv": "Latvian",
   "lt": "Lithuanian",
   "lb": "Luxembourgish",
   "mk": "Macedonian",
   "mg": "Malagasy",
   "ms": "Malay",
   "ml": "Malayalam",
   "mt": "Maltese",
   "mi": "Maori",
   "mr": "Marathi",
   "mn": "Mongolian",
   "my": "Myanmar (Burmese)",
   "ne": "Nepali",
   "no": "Norwegian",
   "or": "Odia (Oriya)",
   "ps": "Pashto",
   "fa": "Persian",
   "pl": "Polish",
   "pt": "Portuguese",
   "pa": "Punjabi",
   "ro": "Romanian",
   "ru": "Russian",
   "sm": "Samoan",
   "gd": "Scots Gaelic",
   "sr": "Serbian",
   "st": "Sesotho",
   "sn": "Shona",
   "sd": "Sindhi",
   "si": "Sinhala",
   "sk": "Slovak",
   "sl": "Slovenian",
   "so": "Somali",
   "es": "Spanish",
   "su": "Sundanese",
   "sw": "Swahili",
   "sv": "Swedish",
   "tg": "Tajik",
   "ta": "Tamil",
   "tt": "Tatar",
   "te": "Telugu",
   "th": "Thai",
   "tr": "Turkish",
   "tk": "Turkmen",
   "uk": "Ukrainian",
   "ur": "Urdu",
   "ug": "Uyghur",
   "uz": "Uzbek",
   "vi": "Vietnamese",
   "cy": "Welsh",
   "xh": "Xhosa",
   "yi": "Yiddish",
   "yo": "Yoruba",
   "zu": "Zulu"
   },
   "al": {}
   }
```


<br><br>

### 代码实现
###### 文件翻译
```python
#!/usr/bin/python
import sys
import time
import os
def main():               
	from pygoogletranslation import Translator
	translator = Translator()
	count = 0
	with open('result.txt', 'w', encoding='gb18030') as df:
	    result = translator.bulktranslate('test.txt', dest="en")
	    df.write(result.text)

if __name__ == "__main__":
	main()
```

<br>

###### 文本翻译
```python
from googletrans import Translator

# 谷歌翻译配置
translator = Translator(service_urls=['translate.google.cn', ])
from pygoogletranslation import Translator

translator = Translator()
trans_text = translator.translate("晚安", dest='en').text
print(trans_text)
```