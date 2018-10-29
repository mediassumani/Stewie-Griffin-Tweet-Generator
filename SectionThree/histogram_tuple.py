""" Modules contains functions to process an histogram of tuple"""
from histogram_dict import frequency

def histogram(source_text):
    split_sentence = []
    tuple_histogram = [()]
    try:
        with open(source_text) as file:
            for line in file:
                split_sentence += line.split()
                for word in split_sentence:
                    tuple_histogram.append((word, frequency(word, split_sentence)))

        file.close()
    except IOError:
        print("Errror Found while opening file")

    return tuple_histogram


def unique_words(tuple_histogram):

    unique_words_count = 0
    filtered_list = []

    for tuple in tuple_histogram:
        for element in tuple:
            if type(element) == str:
                filtered_list.append(element)

    for word in filtered_list:
        if filtered_list.count(word) <=1:
            unique_words_count += 1

    return unique_words_count

def main():
    text_file = "source_text.txt"
    #print(histogram(text_file))
    list = [('one', 1), ('fish', 4), ('two', 1), ('fish', 4), ('red', 1), ('fish', 4), ('blue', 1), ('fish', 4)]
    print(unique_words(list))


if __name__ == "__main__":
    main()
