# -*- coding: utf-8 -*-
import unittest

from siaw import SayItAnotherWay


class TestSayItAnotherWay(unittest.TestCase):

    def setUp(self):
        self.sentence_pinyin = SayItAnotherWay('阿伟死了')
        self.sentence_sequence = SayItAnotherWay('汉字的顺序并不一定能影响阅读')
        self.sentence_reverse = SayItAnotherWay('汉字的顺序并不一定能影响阅读')
        self.sentence_filter = SayItAnotherWay('违禁词会被过滤，比如巨乳，懂了吗？')
        self.sentence_space_mark = SayItAnotherWay('这里会加入一些间隔符号。')
        self.sentence_chaizi = SayItAnotherWay('测试拆字结果。')
        self.sentence_antonym = SayItAnotherWay('测试反义结果。')
        self.sentence_synonym = SayItAnotherWay('测试同义结果。')
        self.sentence_homophone = SayItAnotherWay('测试同音结果。')
        self.sentence_mixed = SayItAnotherWay('测试多种模式混合结果。')

    def test_pinyin_translate(self):
        """测试拼音转换"""
        self.assertEqual(self.sentence_pinyin.translate('pinyin'), 'ā wěi sǐ le')
        self.assertEqual(self.sentence_pinyin.translate('pinyin', style='FIRST_LETTER'), 'awsl')

    def test_sequence_translate(self):
        """测试顺序转换"""
        self.assertEqual(self.sentence_sequence.translate('sequence', use_jieba=False), '汉的字序顺不并定一影能阅响读')

    def test_reverse_translate(self):
        """测试逆序转换"""
        self.assertEqual(self.sentence_reverse.translate('reverse', use_jieba=False), '读阅响影能定一不并序顺的字汉')

    def test_filter_translate(self):
        """测试过滤敏感词转换"""
        self.assertEqual(self.sentence_filter.translate('filter'), '违禁词会被过滤，比如**，懂了吗？')

    def test_space_mark_translate(self):
        """测试添加间隔符转换"""
        self.assertEqual(self.sentence_space_mark.translate('space_mark', use_jieba=False, space_mark='+'),
                         '这+里+会+加+入+一+些+间+隔+符+号+。')

    def test_chaizi_translate(self):
        """测试拆字"""
        self.assertEqual(self.sentence_chaizi.translate('chaizi', use_jieba=False), '水则 言式 手斥 宀子 丝吉 日木 。')

    def test_antonym_translate(self):
        """测试反义"""
        self.assertNotEqual(self.sentence_antonym.translate('antonym'), '测试反义结果。')

    def test_synonym_translate(self):
        """测试同义"""
        self.assertNotEqual(self.sentence_synonym.translate('synonym'), '测试同义结果。')

    def test_homophone_translate(self):
        """测试同音"""
        self.assertNotEqual(self.sentence_homophone.translate('homophone'), '测试同音结果。')

    def test_mixed_translate(self):
        """测试混合模式"""
        self.assertEqual(self.sentence_mixed.translate('mixed', use_jieba=False, space_mark=' ', ways=['chaizi', 'pinyin']),
                         'shuǐzéyánshìxīxīhézhōngmùmòyìgōngshuǐkūnrényīkǒusījírìmù。')
