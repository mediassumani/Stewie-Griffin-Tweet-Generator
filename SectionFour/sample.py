"This Module applies frequency weighting to get likelyhood of an output"

from random import randint
import math
from sys import argv

def sample_by_frequency(histogram):
    """  returns a random word from the dictionary histogram """

    # This list will contain the duplicated words
    duplicated_list = []
    for list in histogram:
        # get the current list
        current_list = list
        count = 0
        while count < (current_list[1] * 2):
            #appending words twice as its original size
            duplicated_list.append(list[0])
            count += 1

    return duplicated_list[randint(0, len(duplicated_list) - 1)]


def main():

    count = 0
    histogram_list = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
    while count < 10:
        print(sample_by_frequency(histogram_list))
        count += 1
if __name__== "__main__":
    main()
