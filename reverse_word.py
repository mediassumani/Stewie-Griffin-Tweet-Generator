import random
import sys

def reverse(str):
 """ Reverses the passed argument of type string"""

    count = len(str) - 1
    while count >= 0:
        print(str[count])
        count -= 1

def main():
    word = sys.argv[1]
    reverse(word)

if __name__ == '__main__':
    main()
