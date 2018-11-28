url = 'http://cs.armstrong.edu/liang/data/Lincoln.txt'.strip()

import urllib.request

infile = urllib.request.urlopen(url)
s = infile.read().decode()

words = [x for x in s.split(' ')]


def removeEmptystrings(x):
    modified_words = []
    for i in range(len(x)):
        if len(words[i]) != 0 and words[i].isalnum():
            modified_words.append(words[i])
    print(len(modified_words), modified_words)

removeEmptystrings(words)

