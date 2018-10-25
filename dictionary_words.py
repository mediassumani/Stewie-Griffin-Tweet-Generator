import sys
import linecache
from random import randint
from algorithm_timer import timing_function


def generateSentence(num_words):
    """ Grabs n random words from the text file"""
    count = 0
    sentence = ""
    try:
        while count < num_words:
            sentence += linecache.getline("/usr/share/dict/words", randint(0, 235885))
            count += 1
    except IOError:
        print("Error Found : Unable to find file")

    return sentence

@timing_function
def tester():
    print(generateSentence(int(sys.argv[1])).replace("\n", " "))
print(tester())

def main():

    tester()

if __name__ == "__main__":
    main()
