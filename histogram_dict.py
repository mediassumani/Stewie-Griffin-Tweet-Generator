import os
import sys



def histogram(source_text):
    """ returns a histogram that stores each unique word with the number of times it appears in the source text"""

    split_sentence = []
    histogram = {}
    try:
        with open(source_text, "r") as file:
            for line in file:
                split_sentence += line.split()
                for word in split_sentence:
                    histogram[word] = 1

        file.close()
        print(frequency("two", histogram))

    except IOError:
        print("Error Found while opening the file")

    return histogram



def unique_words(histogram):
    """ returns the total count of unique words in the histogram"""

    return

def frequency(word, histogram):
    """ returns the number of times that word appears in a text"""
    frequency_count = 0
    for key,value in histogram.items():
        if word.lower() is key or word.capitalize() is key :
            frequency_count += 1
    return frequency_count

def main():

    text_file = "source_text.txt"
    print(histogram(text_file))



if __name__ == "__main__":
    main()
