"""  This module implements Fisher-Yates Shuffle algorithm """

import random


def has_been_shuffled(card, deck):
    """ This function checks """
    return card in deck

def shuffle(deck):
    """ This function shuffles a deck of card"""

    shuffled_deck = []
    for card in deck:
        random_index = random.randint(0, len(deck)-1)
        if (has_been_shuffled(card,shuffled_deck) == False):
            shuffled_deck.append(deck[random_index])

        return shuffled_deck


def main():
    unshuffled_deck = ["Ace","King","Queen","Joker","Diamonds","Hearts","Spades"]

    print("\n\t\tFisher Yates Shuffle Algorithm\n")
    print("Before Shuffle : {}\n".format(unshuffled_deck))
    print("After Shuffle : {}\n".format(shuffle(unshuffled_deck)))

if __name__ == "__main__":
    main()
