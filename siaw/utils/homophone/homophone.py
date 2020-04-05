import os
import random
import pickle
import pkg_resources
from pypinyin import pinyin, Style

dir_path = os.path.dirname(os.path.realpath(__file__))

data = {}
for file_name in ['chinese_homophone_char.txt', 'chinese_homophone_word.txt']:
    with open(os.path.join(dir_path, file_name), 'rt') as fd:
        for line in fd:
            if not line:
                continue
            words = line.strip().split('\t')
            code = words.pop(0)
            code = code.replace('_', ' ')
            data[code] = words

output_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'homophone.pkl')
with open(output_file, 'wb') as fd:
    pickle.dump(data, fd)


class Homophone(object):
    def __init__(self):
        data_file = pkg_resources.resource_filename(__name__, "homophone.pkl")
        with open(data_file, 'rb') as fd:
            self.data = pickle.load(fd)

    def query(self, input_char):
        chars_pinyins = pinyin([input_char], style=Style.NORMAL)
        chars_pinyin = ' '.join(x[0] for x in chars_pinyins)
        homophone_words = self.data.get(chars_pinyin)
        if homophone_words:
            return self._filter(input_char, homophone_words)

        if chars_pinyins[0][0] == input_char:
            return input_char

        result = []
        for index, char_pinyin in enumerate(chars_pinyins):
            char = input_char[index]
            homophone_words = self.data.get(char_pinyin[0])
            result.append(self._filter(char, homophone_words) if homophone_words else char)
        return ''.join(result)

    @staticmethod
    def _filter(source_word, words):
        words = [word for word in words if word and word != source_word]
        if not words:
            return source_word
        return words[random.randint(0, len(words) - 1)]
