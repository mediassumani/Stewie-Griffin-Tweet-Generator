""" Modules contains functions to process an histogram of tuple"""
from algorithm_timer import timing_function

def save_histogram_in_file(histogram):

    try:

        with open("saved_histogram.txt", "w") as file:
            file.write("[ ")
            for tuple in histogram:
                file.write("( {}".format(tuple[0]))
                file.write(" : ")
                file.write("{} ),".format(str(tuple[1])))
            file.write(" ]")
    except IOError:
        print("Error Found : Unable to write on file")


def histogram(source_text):
    tuple_histogram = []
    for word in source_text:
        found_word = False
        for index, tuple in enumerate(tuple_histogram):
            if word == tuple[0]:
                temp_tuple = (word,tuple[1] + 1)
                temp_tuple , tuple = tuple, temp_tuple
                tuple_histogram[index] = tuple
                found_word = True
        if not found_word:
            tuple_histogram.append((word,1))
    return tuple_histogram

def frequency(word, histogram):
    """ returns the number of times that word appears in a text"""
    for tuple in histogram:
        if tuple[0] == word:
            return tuple[1]
    return "{} Not found".format(word)

def unique_words(tuple_histogram):
    """ returns the total count of unique words in the histogram"""
    return len(tuple_histogram)

@timing_function
def tester():
    with open("source_text.txt") as text_file:
        words = text_file.read().replace("\n", "").lower().split()
    created_histogram = histogram(words)
    #print("\n\n\t\t **** HISTOGRAM DATA *** \n\n{}\n\nThere are {} unique words".format(created_histogram, unique_words(created_histogram)))
    save_histogram_in_file(created_histogram)
print(tester())

if __name__ == "__tester__":
    tester()
