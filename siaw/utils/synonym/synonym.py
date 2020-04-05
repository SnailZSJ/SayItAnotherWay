import os
import random
import pickle
import pkg_resources

dir_path = os.path.dirname(os.path.realpath(__file__))

data = {'code2words': {}, 'word2code': {}}
with open(os.path.join(dir_path, 'dict_synonym.txt'), 'rt') as fd:
    for line in fd:
        if not line:
            continue
        split_char = ''
        for char in ['@', '=', '#']:
            if char in line:
                split_char = char
                break
        if not split_char:
            continue
        code, words = line.strip().split(split_char)
        words = words.strip('').split(' ')
        data['code2words'][code] = words
        for word in words:
            data['word2code'][word] = code

output_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'synonym.pkl')
with open(output_file, 'wb') as fd:
    pickle.dump(data, fd)


class Synonym(object):
    def __init__(self):
        data_file = pkg_resources.resource_filename(__name__, "synonym.pkl")
        with open(data_file, 'rb') as fd:
            self.data = pickle.load(fd)

    def query(self, input_char):
        synonym_code = self.data['word2code'].get(input_char, '')
        if not synonym_code:
            return input_char
        synonym_words = self.data['code2words'].get(synonym_code, [])
        synonym_words = [word for word in synonym_words if word and word != input_char]
        if not synonym_words:
            return input_char
        return synonym_words[random.randint(0, len(synonym_words) - 1)]
