""" Modules contains functions to process an histogram of dictionary"""

from algorithm_timer import timing_function

def histogram(source_text):
    "Returns a dictionary histogram data structure that stores each unique word along with its freqeuncy"
    dict_histogram = {}
    for word in source_text:
        # if the word is already in the dict, we increment its freqeuncy
        if word in dict_histogram:
            #Increments its freqeuncy,
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
    print("\n\n\t\t **** HISTOGRAM DATA *** \n\n{}\n\nThere are {} unique words".format(created_histogram, unique_words(created_histogram)))
print(tester())

if __name__ == "__tester__":
    tester()
