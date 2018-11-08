"""Optimized to grab wp"""

import sys
import linecache
from random import randint


def generateSentence(num_words):
    """ Returns n random words from the text file"""
    count = 0
    sentence = ""
    total_words = 235885
    random_line = "/usr/share/dict/words"
    try:
        while count < num_words:
            sentence += linecache.getline(random_line, randint(0, total_words))
            count += 1
    except IOError:
        print("Error Found : Unable to find file")

    return sentence
