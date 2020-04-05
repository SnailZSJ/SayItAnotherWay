import os
import pickle
import pkg_resources

dir_path = os.path.dirname(os.path.realpath(__file__))

data = {}
with open(os.path.join(dir_path, 'dict_antonym.txt'), 'rt') as fd:
    for line in fd:
        if not line:
            continue
        source, target = line.strip().split(':')
        data[source] = target
        data[target] = source

output_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'antonym.pkl')
with open(output_file, 'wb') as fd:
    pickle.dump(data, fd)


class Antonym(object):
    def __init__(self):
        data_file = pkg_resources.resource_filename(__name__, "antonym.pkl")
        with open(data_file, 'rb') as fd:
            self.data = pickle.load(fd)

    def query(self, input_char):
        result = self.data.get(input_char, input_char)
        return result
