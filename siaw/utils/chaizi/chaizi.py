import os
import pickle
import pkg_resources

dir_path = os.path.dirname(os.path.realpath(__file__))

data = {}
for file_name in ['chaizi-ft.txt', 'chaizi-jt.txt']:
    with open(os.path.join(dir_path, file_name), 'rt') as fd:
        for line in fd:
            item_list = line.strip().split('\t')
            key = item_list[0]
            value = [i.strip().split() for i in item_list[1:]]
            data[key] = value

output_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chaizi.pkl')
with open(output_file, 'wb') as fd:
    pickle.dump(data, fd)


class Chaizi(object):
    def __init__(self):
        data_file = pkg_resources.resource_filename(__name__, "chaizi.pkl")
        with open(data_file, 'rb') as fd:
            self.data = pickle.load(fd)

    def query(self, input_char):
        result = self.data.get(input_char, input_char)
        return result[0]


if __name__ == "__main__":
    hc = Chaizi()
    result = hc.query('名')
    print(result)
