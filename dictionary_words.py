import sys
import random
import linecache

def main():

    print(generateSentence(int(sys.argv[1])).replace("\n", " "))

def generateSentence(num_of_words):
    count = 0
    sentence = ""
    try:
        while count < num_of_words:
            sentence += linecache.getline("/usr/share/dict/words", random.randint(0, 235885))
            count += 1

    except IOError:
        print("Error Found : Unable to find file")

    return sentence


if __name__ == "__main__":
    main()
