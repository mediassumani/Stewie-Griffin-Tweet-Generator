""" Modules contains functions to process an histogram of tuple"""
from histogram_dict import frequency

def histogram(source_text):
    split_sentence = []
    histogram = [()]
    try:
        with open(source_text) as file:
            for line in file:
                split_sentence += line.split()
                for word in split_sentence:
                    histogram.append((word, frequency(word, split_sentence)))

        file.close()
    except IOError:
        print("Errror Found while opening file")

    return histogram


def unique_words(histogram):


def main():
    text_file = "source_text.txt"
    print(histogram(text_file))

if __name__ == "__main__":
    main()
