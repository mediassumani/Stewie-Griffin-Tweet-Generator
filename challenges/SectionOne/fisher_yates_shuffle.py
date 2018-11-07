"""  This module implements Fisher-Yates Shuffle algorithm """

import random
from algorithm_timer import timing_function

def shuffle(deck):
    """ This function shuffles a deck of card"""
    shuffled_deck = []
    count = len(deck)

    while(count):
        random_index = random.randint(0, len(deck)-1)
        if deck[random_index] not in shuffled_deck:
            shuffled_deck.append(deck[random_index])
            count -= 1
    return shuffled_deck

@timing_function
def tester():

    unshuffled_deck = ["Ace","King","Queen","Joker","Diamonds","Hearts","Spades"]
    print("\n\t\tFisher Yates Shuffle Algorithm\n")
    print("Before Shuffle : {}\n".format(unshuffled_deck))
    print("After Shuffle : {}\n".format(shuffle(unshuffled_deck)))
print(tester())

if __name__ == "__tester__":
    tester()
