import re
import sys
import requests
from validators import url
from collections import Counter


def load_data(file_location):
    if url(file_location):
        r = requests.get(file_location)
        return r.text
    else:
        with open(file_location, 'r', encoding='utf-8') as f:
            return f.read()


def get_most_frequent_words(text):
    showed_frequent_words = 10
    words_list = re.split('\W*\s\W*', text.lower())
    return Counter(words_list).most_common(showed_frequent_words)


def print_most_frequent_words(words_dict):
    print('The most frequent words in this text are:\n{0:^20s} | {1:^8s}'
          .format("WORDS", "COUNTS"))
    for word, count in words_dict:
        print('{0:^20s} | {1:^8d}'.format(word, count))


if __name__ == '__main__':
    filepath = sys.argv[1]
    words_dict = get_most_frequent_words(load_data(filepath))
    print_most_frequent_words(words_dict)
