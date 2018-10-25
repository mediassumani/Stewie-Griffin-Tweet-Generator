import sys
import random
import linecache

def main():

    print(generateSentence(6))

def generateSentence(num_of_words):
    count = 0
    sentence = ""
    rand_index = random.randint(0, 235885)
    try:
        while count <= num_of_words:
            sentence += linecache.getline("/usr/share/dict/words", rand_index)
            count += 1

    return sentence
    except IOError:
        print("Error Found : Unable to find file")


if __name__ == "__main__":
    main()
