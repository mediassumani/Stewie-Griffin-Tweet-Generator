""" Modules contains functions to process an histogram of dictionary"""
config_file = '/Users/mediassumani/Documents/dev/cs/Courses/CS1.2/algorithm_timer.py'
import sys
import os
sys.path.append(os.path.dirname(config_file))
from algorithm_timer import timing_function

def histogram(source_text):
    """ returns a histogram that stores each unique word with the number of times it appears in the source text"""

    split_sentence = []
    dict_histogram = {}
    try:
        with open(source_text, "r") as file:
            for line in file:
                print(line.split())

        file.close()
    except IOError:
        print("Error Found while opening the file")
    print("There are {} unique words in this histogram".format(unique_words(dict_histogram)))
    return dict_histogram

def unique_words(histogram):
    """ returns the total count of unique words in the histogram"""

    unique_words_count = 0
    for key,value in histogram.items():
        if value == 1:
            unique_words_count += 1

    return unique_words_count

def frequency(word, text):
    """ returns the number of times that word appears in a text"""
    frequency_count = 0
    for str in text:
        if word == str.lower() or word == str.upper() or word == str+".":
            frequency_count += 1

    return frequency_count


@timing_function
def tester():
    text_file = "source_text.txt"
    print(histogram(text_file))
print(tester())


if __name__ == "__tester__":
    tester()
