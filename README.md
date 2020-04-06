# 换种说法

> 同一句话有不同的表达方式，有时候需要翻译翻译。

* GitHub: https://github.com/SnailZSJ/SayItAnotherWay
* License: MIT license
* PyPI: https://pypi.org/project/siaw/
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
pip3 install siaw
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

sentence_sequence = SayItAnotherWay("汉字的顺序并不一定能影响阅读")
result = sentence_sequence.translate('sequence', use_jieba=False)

print(result)
```

输出

```text
'汉的字序顺不并定一影能阅响读'
```

#### 3. 逆序转换
```python
from siaw import SayItAnotherWay

sentence_reverse = SayItAnotherWay("汉字的顺序并不一定能影响阅读")
result = sentence_reverse.translate('reverse', use_jieba=False)

print(result)
```

输出

```text
'读阅响影能定一不并序顺的字汉'
```

#### 4. 过滤敏感词转换
```python
from siaw import SayItAnotherWay

sentence_filter = SayItAnotherWay("违禁词会被过滤，比如巨乳，懂了吗？")
result = sentence_filter.translate('filter')

print(result)
```

输出

```text
'违禁词会被过滤，比如**，懂了吗？'
```

#### 5. 添加间隔符转换
```python
from siaw import SayItAnotherWay

sentence_space_mark = SayItAnotherWay("这里会加入一些间隔符号。")
result = sentence_space_mark.translate('space_mark', use_jieba=False, space_mark='+')

print(result)
```

输出

```text
'这+里+会+加+入+一+些+间+隔+符+号+。'
```

#### 6. 拆字转换
```python
from siaw import SayItAnotherWay

sentence_chaizi = SayItAnotherWay("测试拆字结果。")
result = sentence_chaizi.translate('chaizi', use_jieba=False)

print(result)
```

输出

```text
'水则 言式 手斥 宀子 丝吉 日木 。'
```

#### 7. 反义转换
```python
from siaw import SayItAnotherWay

sentence_antonym = SayItAnotherWay("Python从入门到放弃。")
result = sentence_antonym.translate('antonym')

print(result)
```

输出

```text
'Python主入门到坚持。'
```

#### 8. 同义转换
```python
from siaw import SayItAnotherWay

sentence_synonym = SayItAnotherWay("Python从入门到放弃。")
result = sentence_synonym.translate('synonym')

print(result)
```

输出

```text
'Python打入库及割舍。'
```

#### 9. 同音转换
```python
from siaw import SayItAnotherWay

sentence_homophone = SayItAnotherWay("苟利国家生死以，岂因福祸避趋之。")
result = sentence_homophone.translate('homophone')

print(result)
```

输出

```text
'煹鷅濄扴狌蟖齮，埼音俘获比娶支。'
```

#### 10. 测试混合模式转换
```python
from siaw import SayItAnotherWay

sentence_mixed = SayItAnotherWay("测试多种模式混合结果。")
result = sentence_mixed.translate('mixed', use_jieba=False, space_mark=' ', ways=['chaizi', 'pinyin'])

print(result)
```

输出

```text
'shuǐzéyánshìxīxīhézhōngmùmòyìgōngshuǐkūnrényīkǒusījírìmù。'
```

## TODO
1. 提高同、反义词的准确性和词量。
2. 提供更简明便捷通用的 API 接口。
3. 降低打包后的文件体积。
4. ...

## 致谢
- [结巴中文分词](https://github.com/fxsjy/jieba)
- [汉字转拼音](https://github.com/mozillazg/python-pinyin)
- [敏感词过滤](https://github.com/observerss/textfilter)
- [汉字拆字库](https://github.com/howl-anderson/hanzi_chaizi)
- [同义词表，反义词表，否定词表](https://github.com/guotong1988/chinese_dictionary)
- [中文谐音词/字库（同音词/字）](https://github.com/LiangsLi/ChineseHomophones)