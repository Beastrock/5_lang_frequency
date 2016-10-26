import collections
import re
import requests
import sys


def load_data(file_location):
    if '://' in file_location:
        r = requests.get(file_location)
        text = r.text
        return text
    else:
        with open(file_location, 'r', encoding='utf-8') as f:
            text = f.read()
            return text


def get_most_frequent_words(text):
    lower_text = text.lower()
    list_of_words = re.split('\W*\s\W*', lower_text)
    print(list_of_words)
    dict_of_words = collections.Counter(list_of_words)
    for word, count in dict_of_words.most_common(10):
        print('%s : %5d' % (word, count))
    return


if __name__ == '__main__':
    file_location = sys.argv[1]
    get_most_frequent_words(load_data(file_location))
