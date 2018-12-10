from random import choice
from dictogram import Dictogram
from stochatic_sample import dict_frequency_sample
from file_opener import read_file
from histogram_generator import generate_histogram
from collections import deque

class Second_Markov(dict):

    def __init__(self, word_list, order=1, original=True):
        super(Second_Markov, self).__init__()
        

    # def _create_model(self):
    #     histogram = self._create_histogram()
    #     markov_model = {}
    #
    #     for key,value in histogram.items():
    #         temp_value = {}
    #         if key not in markov_model:
    #             temp_key = (key, "")
    #             for i in range(0, len(self.words)-1):
    #                 temp_word = self.words[i]
    #                 if temp_word == temp_key[0]:
    #                     temp_key = (key, self.words[i+1])
    #                     temp_value[(temp_key[1], )]
    #
    #         markov_model[temp_key] = temp_value
    #
    #
    #
    # def generate_sentence(self):
    #     pass


text_list = read_file("iwent_youwent.txt")
histogram = generate_histogram(text_list)
model = Second_Markov(text_list, histogram, 1, True)
