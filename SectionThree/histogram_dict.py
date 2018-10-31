""" Modules contains functions to process an histogram of dictionary"""

config_file = '/Users/mediassumani/Documents/dev/cs/Courses/CS1.2/algorithm_timer.py'
import sys
import os
sys.path.append(os.path.dirname(config_file))
from algorithm_timer import timing_function

def histogram(source_text):
    "returns a histogram data structure that stores each unique word along with the number of times the word appears in the text"
    dict_histogram = {}
    for word in source_text:
        # if the word is already in the dict, we increment its freqeuncy, else add 1 freq.
        if word in dict_histogram:
            dict_histogram[word] += 1
        else:
            dict_histogram[word] = 1

    return dict_histogram


def unique_words(histogram):
    """ returns the total count of unique words in the histogram"""
    return len(histogram)

def frequency(word, histogram):
    """ returns the number of times that word appears in a text"""
    for key,value in histogram.items():
        if key == word:
            return value
        else:
            return "The word {} is not found".format(word)

@timing_function
def tester():

    with open("source_text.txt") as text_file:
        words = text_file.read().replace("\n", "").lower().split()
    created_histogram = histogram(words)
    print("\n\n\t\t **** HISTOGRAM DATA *** \n\n{}\n\nThere are {} unique words\n".format(created_histogram, unique_words(created_histogram)))
    print("The word fish is spotted {} times.".format(frequency("fish", created_histogram)))


print(tester())


if __name__ == "__tester__":
    tester()
