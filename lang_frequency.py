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
    words_list = re.split('\W*\s\W*', text.lower())
    words_dict = collections.Counter(words_list)
    return words_dict


def print_most_frequent_words(words_dict, showed_frequent_words):
    print('The most frequent words in this text are:')
    for word, count in words_dict.most_common(showed_frequent_words):
        print("{}:  {}".format(count, word))
    return


if __name__ == '__main__':
    text = load_data(sys.argv[1])
    words_dict = get_most_frequent_words(text)
    try:
        showed_frequent_words = sys.argv[2]
    except LookupError:
        showed_frequent_words = 10
    print_most_frequent_words(words_dict, showed_frequent_words)

