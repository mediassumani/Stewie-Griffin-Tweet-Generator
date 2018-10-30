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
                if line == "":
                    pass
                else:
                    split_sentence += line.split()
                    for word in split_sentence:
                        temp_word = word.replace(".","")
                        dict_histogram[temp_word.replace(",","")] = frequency(temp_word.replace(",",""), split_sentence)

        # print(dict_histogram)
        file.close()
    except IOError:
        print("Error Found while opening the file")
    print("\nThere are {} unique words in this histogram\n".format(unique_words(dict_histogram)))
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
        temp_str = str.replace(".","")
        if word == temp_str.replace(",","").lower() or word == temp_str.replace(",","").upper():
            frequency_count += 1

    return frequency_count


@timing_function
def tester():
    text_file = "source_text.txt"
    print(histogram(text_file))
print(tester())


if __name__ == "__tester__":
    tester()
