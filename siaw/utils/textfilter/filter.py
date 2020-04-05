# -*- coding:utf-8 -*-
from collections import defaultdict
import re
import os
import pickle
import pkg_resources

__all__ = ['NaiveFilter', 'BSFilter', 'DFAFilter']
__author__ = 'observer'
__date__ = '2012.01.05'

source_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'keywords.txt')
output_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'keywords.pkl')

data = []
with open(source_path, 'rt') as f:
    for word in f:
        data.append(word.strip().lower())

with open(output_file, 'wb') as fd:
    pickle.dump(data, fd)


class BaseFilter(object):
    '''Filter Messages from keywords

    Use Back Sorted Mapping to reduce replacement times

    >>> f = BaseFilter()
    >>> f.add("sexy")
    >>> f.filter("hello sexy baby")
    hello **** baby
    '''
    def __init__(self):
        data_file = pkg_resources.resource_filename(__name__, 'keywords.pkl')
        with open(data_file, 'rb') as f:
            self.keywords = pickle.load(f)

    def add(self, keyword):
        keyword = keyword.lower()
        if keyword not in self.keywords:
            self.keywords.add(keyword)

    def filter(self, message, repl="*"):
        message = message.lower()
        for kw in self.keywords:
            message = message.replace(kw, repl * len(kw))
        return message


class NaiveFilter(BaseFilter):
    pass


class BSFilter(BaseFilter):

    def __init__(self):
        super(BSFilter, self).__init__()
        self.kwsets = set(self.keywords)
        self.pat_en = re.compile(r'^[0-9a-zA-Z]+$')  # english phrase or not
        self.bsdict = defaultdict(set)

        for index, keyword in enumerate(self.keywords):
            for word in keyword.split():
                if self.pat_en.search(word):
                    self.bsdict[word].add(index)
                    continue
                for char in word:
                    self.bsdict[char].add(index)

    def add(self, keyword):
        keyword = keyword.lower()
        if keyword in self.kwsets:
            return
        self.keywords.append(keyword)
        self.kwsets.add(keyword)
        index = len(self.keywords) - 1
        for word in keyword.split():
            if self.pat_en.search(word):
                self.bsdict[word].add(index)
                continue
            for char in word:
                self.bsdict[char].add(index)

    def filter(self, message, repl="*"):
        message = message.lower()
        for word in message.split():
            if self.pat_en.search(word):
                for index in self.bsdict[word]:
                    message = message.replace(self.keywords[index], repl * len(self.keywords[index]))
                continue
            for char in word:
                for index in self.bsdict[char]:
                    message = message.replace(self.keywords[index], repl * len(self.keywords[index]))
        return message


class DFAFilter(BaseFilter):

    def __init__(self):
        super(DFAFilter, self).__init__()
        self.keyword_chains = {}
        self.delimit = '\x00'
        for keyword in self.keywords:
            self.add(keyword)

    def add(self, keyword):
        keyword = keyword.lower()
        chars = keyword.strip()
        if not chars:
            return
        level = self.keyword_chains
        i = 0
        for i in range(len(chars)):
            if chars[i] not in level:
                if not isinstance(level, dict):
                    break
                last_level = level
                last_char = chars[-1]
                for j in range(i, len(chars)):
                    level[chars[j]] = {}
                    last_level, last_char = level, chars[j]
                    level = level[chars[j]]
                last_level[last_char] = {self.delimit: 0}
                break
            level = level[chars[i]]
        if i == len(chars) - 1:
            level[self.delimit] = 0

    def filter(self, message, repl="*"):
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char not in level:
                    ret.append(message[start])
                    break
                step_ins += 1
                if self.delimit in level[char]:
                    ret.append(repl * step_ins)
                    start += step_ins - 1
                    break
                level = level[char]
            else:
                ret.append(message[start])
            start += 1
        return ''.join(ret)
