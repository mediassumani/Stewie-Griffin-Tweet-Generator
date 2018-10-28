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
                    histogram[word] = frequency(word, split_sentence)

        file.close()

    except IOError:
        print("Error Found while opening the file")

    return histogram



def unique_words(histogram):
    """ returns the total count of unique words in the histogram"""

    unique_words_count = 0
    words = []
    for key,value in histogram.items():
        words.append(key)

    for word in words:
        if words.count(word) <= 1:
            unique_words_count += 1

    return unique_words_count

def frequency(word, text):
    """ returns the number of times that word appears in a text"""
    frequency_count = 0
    for str in text:
        if word == str.lower() or word.upper() == str.upper():
            frequency_count += 1

    return frequency_count

def main():

    text_file = "source_text.txt"
    print(histogram(text_file))

if __name__ == "__main__":
    main()
