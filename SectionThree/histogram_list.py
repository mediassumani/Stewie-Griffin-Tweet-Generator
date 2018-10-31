def histogram(source_text):
    "returns a dictionary histogram data structure that stores each unique word along with the number of times the word appears in the text"
    list_histogram = []
    for word in source_text:
        found_word = False
        for histogram in list_histogram:
            if word == histogram[0]:
                histogram[1] = histogram[1] + 1
                found_word = True
                break
        if not found_word:
            list_histogram.append([word, 1])
    return list_histogram

def frequency(word, histogram):
    """ returns the number of times that word appears in a text"""
    for array in histogram:
        if array[0] == word:
            return array[1]

def unique_words(tuple_histogram):
    """ returns the total count of unique words in the histogram"""
    return len(tuple_histogram)

def main():
    with open("source_text.txt") as text_file:
        words = text_file.read().replace("\n", "").lower().split()
    created_histogram = histogram(words)
    print("\n\n\t\t **** HISTOGRAM DATA *** \n\n{}\n\nThere are {} unique words".format(created_histogram, unique_words(created_histogram)))
    print("The word one appears {} times in the histogram".format(frequency("one",created_histogram)))



if __name__ == "__main__":
    main()
