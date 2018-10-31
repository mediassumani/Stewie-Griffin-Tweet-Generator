""" Modules contains functions to process an histogram of tuple"""
def histogram(source_text):
    tuple_histogram = []
    for word in source_text:
        found_word = False
        for index, tuple in enumerate(tuple_histogram):
            if word == tuple[0]:
                temp_tuple = (word,tuple[1] + 1)
                temp_tuple, tuple = tuple, temp_tuple
                tuple_histogram[index] = tuple
                found_word = True
                break
        if not found_word:
            tuple_histogram.append((word,1))

    return tuple_histogram

def frequency(word, histogram):
    for tuple in histogram:
        if tuple[0] == word:
            return tuple[1]
    return "{} Not found".format(word)

def unique_words(tuple_histogram):
    return len(tuple_histogram)

def main():
    with open("source_text.txt") as text_file:
        words = text_file.read().replace("\n", "").lower().split()
    created_histogram = histogram(words)
    print("\n\n\t\t **** HISTOGRAM DATA *** \n\n{}\n\nThere are {} unique words".format(created_histogram, unique_words(created_histogram)))
    print("The word fish appears {} times in the histogram".format(frequency("fish",created_histogram)))





if __name__ == "__main__":
    main()
