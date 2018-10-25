import sys
import os
import random

def main():

    generateSentence(6)

def generateSentence(num_of_words):

    file_path = '/usr/share/dict/words'
    file_size = 0
    rand_index = random.randint(0, 235885)
    try:
        with open(file_path, 'r') as text_file:
            for line in text_file:
                print(len(str(line)))

    except IOError:
        print("Error Found : Unable to find file")

if __name__ == "__main__":
    main()
