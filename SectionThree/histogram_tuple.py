""" Modules contains functions to process an histogram of tuple"""
def histogram(source_text):
    tuple_histogram = [()]

    for word in source_text:
    # tuple_histogram.append((word, frequency(word, split_sentence)))
        if 

    pass

def frequency(word, histogram):
    return 1

def unique_words(tuple_histogram):
    pass

def main():

    with open("source_text.txt") as text_file:
        words = text_file.read().replace("\n", "").lower().split()
    created_histogram = histogram(words)

if __name__ == "__main__":
    main()
