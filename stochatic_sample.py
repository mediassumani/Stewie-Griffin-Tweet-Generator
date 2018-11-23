""" This module contains one method to randomly select
 a word from an histogram based on its frequency
 """

import random

def list_frequency_sample(histogram):
    """ Returns a random word based on its weight
        @param:
            - histogram : the histogram that contains the words and their frequencies.
    """

    accumulator = 0
    total_tokens = 0
    for list in histogram:
        total_tokens += list[1]

    random_integer = random.randint(1,total_tokens)
    for list in histogram:
        accumulator += list[1]
        if accumulator >= random_integer:
            return list[0]

def dict_frequency_sample(histogram):
    accumulator = 0
    total_tokens = len(histogram)
    random_integer = random.randint(1,total_tokens)

    for key,value in histogram.items():
        accumulator += value
        if accumulator >= random_integer:
            return key
