""" Module to create sentences"""
from stochatic_sample import dict_frequency_sample

def generate_sentence(histogram, num_of_words):
    """ Returns  a sentence based on its word freqencies """

    sentence = " "
    for _ in range(0, num_of_words):
        sentence += dict_frequency_sample(histogram) + " "
    if num_of_words == 0:
        raise Exception("No Amount of words passed")
    return sentence
