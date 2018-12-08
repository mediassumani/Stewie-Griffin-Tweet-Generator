from random import choice
from dictogram import Dictogram
from stochatic_sample import dict_frequency_sample
from file_opener import read_file
from histogram_generator import generate_histogram

class Second_Markov(dict):

    def __init__(self, word_list):
        super(Second_Markov).__init__()
        self.words = word_list
        self.sentence = ""

    def _create_histogram(self):
        return generate_histogram(self.words)

    def _create_model(self):
        pass

    def generate_sentence(self):
        pass


text_list = read_file("stewi_griffin_scripts.txt")
markov_model = Second_Markov(text_list)
print(markov_model._create_histogram())
