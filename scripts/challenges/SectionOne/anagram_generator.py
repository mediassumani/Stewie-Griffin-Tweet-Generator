"""  Simpple anagram generator using random indexes"""

import random
import sys

def generate_anagram(word):
    new_word = ""
    for letter in word:
        new_word += word[random.randint(0,len(word) - 1)]
    return new_word

def main():
    print("Generated anagram : {}".format(generate_anagram(sys.argv[1])))

if __name__ == "__main__":
    main()
