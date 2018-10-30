""" Modules contains functions to process an histogram of dictionary"""


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
                        dict_histogram[word] = frequency(word, split_sentence)

        file.close()
    except IOError:
        print("Error Found while opening the file")
    print(unique_words(dict_histogram))
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
        if word == str.lower() or word.upper() == str.upper():
            frequency_count += 1

    return frequency_count

def main():
    text_file = "source_text.txt"
    histogram(text_file)


if __name__ == "__main__":
    main()
