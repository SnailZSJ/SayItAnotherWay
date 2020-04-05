
import jieba
from pypinyin import pinyin, Style

from .utils.textfilter.filter import DFAFilter
from .utils.chaizi.chaizi import Chaizi
from .utils.antonym.antonym import Antonym
from .utils.synonym.synonym import Synonym
from .utils.homophone.homophone import Homophone

jieba.enable_paddle()


class SayItAnotherWay(object):

    def __init__(self, sentence):
        self.sentence = sentence
        self.words = []

    def __str__(self):
        return self.sentence

    def translate(self, way, *args, **kwargs):
        if not hasattr(self, f'{way}_translate'):
            raise Exception('way error!')
        if not self.words or kwargs.get('refresh', False):
            self.refresh(*args, **kwargs)
        return getattr(self, f'{way}_translate')(*args, **kwargs)

    def refresh(self, *args, **kwargs):
        self.cut(*args, **kwargs)

    def mixed_translate(self, *args, **kwargs):
        words = kwargs.pop('words', self.words)
        ways = kwargs.pop('ways', [])
        if not ways:
            return ''.join(words)
        for way in ways:
            if not hasattr(self, f'_{way}_translate'):
                raise Exception('way error!')
            words = getattr(self, f'_{way}_translate')(words, *args, **kwargs)
        return ''.join(words)

    def pinyin_translate(self, *args, **kwargs):
        """拼音、首字母"""
        words = kwargs.pop('words', self.words)
        space_mark = '' if 'style' in kwargs else ' '
        style = getattr(Style, kwargs.pop('style', 'TONE'))
        return space_mark.join(self._pinyin_translate(words, *args, style=style, space_mark=space_mark, **kwargs))

    def _pinyin_translate(self, words, *args, style=Style.TONE, space_mark=' ', **kwargs):
        result = pinyin(words, style=style)
        return [space_mark.join(item) for item in result]

    def sequence_translate(self, *args, **kwargs):
        """打乱顺序"""
        words = kwargs.pop('words', self.words)
        result = self._sequence_translate(words, *args, **kwargs)
        return ''.join(result)

    def _sequence_translate(self, words, *args, **kwargs):
        result = [words[0]]
        total_num = len(words)
        for i in range(1, total_num, 2):
            if i + 1 != total_num:
                result.append(words[i + 1][::-1])
            result.append(words[i][::-1])
        return result

    def reverse_translate(self, *args, **kwargs):
        """逆序"""
        words = kwargs.pop('words', self.words)
        return ''.join(self._reverse_translate(words, *args, **kwargs))

    def _reverse_translate(self, words, *args, **kwargs):
        return [word[::-1] for word in words[::-1]]

    def filter_translate(self, *args, **kwargs):
        """过滤敏感词"""
        words = kwargs.pop('words', self.words)
        return ''.join(self._filter_translate(words, *args, **kwargs))

    def _filter_translate(self, words, *args, replace_str='*', **kwargs):
        gfw = DFAFilter()
        return [gfw.filter(word, replace_str) for word in words]

    def space_mark_translate(self, *args, **kwargs):
        """添加间隔符"""
        words = kwargs.pop('words', self.words)
        space_mark = kwargs.pop('space_mark', '-')
        return ''.join(self._space_mark_translate(words, space_mark, *args, **kwargs))

    def _space_mark_translate(self, words, space_mark, *args, **kwargs):
        result = []
        for word in words:
            result.append(word)
            result.append(space_mark)
        return result[:-1]

    def chaizi_translate(self, *args, **kwargs):
        """拆字"""
        words = kwargs.pop('words', self.words)
        return ' '.join(self._chaizi_translate(words, *args, **kwargs))

    def _chaizi_translate(self, words, *args, **kwargs):
        chaizi = Chaizi()
        return [''.join(chaizi.query(char)) for word in words for char in word]

    def antonym_translate(self, *args, **kwargs):
        """反义"""
        words = kwargs.pop('words', self.words)
        antonym = Antonym()
        return ''.join(self._antonym_translate(words, *args, **kwargs))

    def _antonym_translate(self, words, *args, **kwargs):
        antonym = Antonym()
        return [''.join(antonym.query(word)) for word in words]

    def synonym_translate(self, *args, **kwargs):
        """同义"""
        words = kwargs.pop('words', self.words)
        return ''.join(self._synonym_translate(words, *args, **kwargs))

    def _synonym_translate(self, words, *args, **kwargs):
        synonym = Synonym()
        return [''.join(synonym.query(word)) for word in words]

    def homophone_translate(self, *args, **kwargs):
        """同音"""
        words = kwargs.pop('words', self.words)
        return ''.join(self._homophone_translate(words, *args, **kwargs))

    def _homophone_translate(self, words, *args, **kwargs):
        homophone = Homophone()
        return ''.join(''.join(homophone.query(word)) for word in words)

    def cut(self, *args, **kwargs):
        if kwargs.get('use_jieba', True):
            self.words = self._jieba_cut(cut_all=kwargs.get('cut_all', False))
        else:
            self.words = self._normal_cout()

    def _jieba_cut(self, cut_all=False):
        return list(jieba.cut(self.sentence, cut_all=cut_all))

    def _normal_cout(self):
        return list(self.sentence)
