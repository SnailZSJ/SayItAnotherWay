# 换种说法

> 同一句话有不同的表达方式，有时候需要翻译翻译。

* GitHub: https://github.com/SnailZSJ/SayItAnotherWay
* License: MIT license
* PyPI: 
* Python version: pypy3, 3.6, 3.7, 3.8

## 已支持功能列表

| 功能 | 参数 |
| ---- | ---- |
| 拼音转换 | pinyin |
| 顺序转换 | sequence |
| 逆序转换 | reverse |
| 过滤敏感词转换 | filter |
| 添加间隔符转换 | space_mark |
| 拆字转换 | chaizi |
| 反义词转换 | antonym |
| 同义词转换 | synonym |
| 同音转换 | homophone |

## 安装
```
pip install siaw
```

## 使用示例

#### 1. 拼音转换
```python
from siaw import SayItAnotherWay

sentence_pinyin = SayItAnotherWay("阿伟死了")
result = sentence_pinyin.translate('pinyin')

print(result)
```

输出

```text
'ā wěi sǐ le'
```

#### 2. 乱序转换
```python
from siaw import SayItAnotherWay

sentence_pinyin = SayItAnotherWay("汉字的顺序并不一定能影响阅读")
result = sentence_pinyin.translate('translate', use_jieba=False)

print(result)
```

输出

```text
'汉的字序顺不并定一影能阅响读'
```

## 致谢
- [结巴中文分词](https://github.com/fxsjy/jieba)
- [汉字转拼音](https://github.com/mozillazg/python-pinyin)
- [敏感词过滤](https://github.com/observerss/textfilter)
- [汉字拆字库](https://github.com/howl-anderson/hanzi_chaizi)
- [同义词表，反义词表，否定词表](https://github.com/guotong1988/chinese_dictionary)
- [中文谐音词/字库（同音词/字）](https://github.com/LiangsLi/ChineseHomophones)