""" Modules contains functions to process an histogram of list"""
from algorithm_timer import timing_function

def histogram(source_text):
    """returns a dictionary histogram data structure that stores each unique word along with the number of times the word appears in the text
    @param:
        - source_text : the corpus to create the histogram from

    @return
        - list_histogram : The created histogram
    """
    list_histogram = []
    for word in source_text:
        found_word = False
        for list in list_histogram:
            # increments the frequency of the word if already seen
            if word == list[0]:
                list[1] = list[1] + 1
                found_word = True
                break
        if not found_word:
            # gives a frequency of 1 if word never seen before
            list_histogram.append([word, 1])

    return list_histogram

def frequency(word, histogram):
    """ returns the number of times that word appears in a text"""
    for list in histogram:
        # if word is seen, returns its frequency
        if array[0] == word:
            return array[1]

    return 0 # returns zero if the word is not in histogram

def unique_words(tuple_histogram):
    """ returns the total count of unique words in the histogram"""
    return len(tuple_histogram)

def main():

    # Testing the methods created above
    with open("source_text.txt") as text_file:
        words = text_file.read().replace("\n", "").lower().split()
    created_histogram = histogram(words)
    print("\n\n\t\t **** HISTOGRAM DATA *** \n\n{}\n\nThere are {} unique words".format(created_histogram, unique_words(created_histogram)))
    print("The word one appears {} times in the histogram".format(frequency("one",created_histogram)))


if __name__ == "__main__":
    main()
