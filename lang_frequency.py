from collections import Counter
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
    showed_frequent_words = 10
    words_list = re.split('\W*\s\W*', text.lower())
    return Counter(words_list).most_common(showed_frequent_words)


def print_most_frequent_words(words_dict):
    print('The most frequent words in this text are:')
    for word, count in words_dict:
        print("{}:  {}".format(count, word))
    return


if __name__ == '__main__':
    filepath = sys.argv[1]
    words_dict = get_most_frequent_words(load_data(filepath))
    print_most_frequent_words(words_dict)
