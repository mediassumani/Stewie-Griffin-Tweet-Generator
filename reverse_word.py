import random
import sys

def reverse(word):
 """ Reverses the passed argument of type string"""

    count = len(word) - 1
    while count >= 0:
        print(word[count])
        count -= 1

def main():
    word = sys.argv[1]
    reverse(word)

if __name__ == '__main__':
    main()
