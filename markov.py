from random import choice
from dictogram import Dictogram
from stochatic_sample import dict_frequency_sample
from file_opener import read_file
from histogram_generator import generate_histogram


class Markov(dict):

    def __init__(self, word_list):
        super(Markov, self).__init__()
        self.order = 1
        self.words = word_list
        self.sentence = ""

    def _create_histogram(self):
        return generate_histogram(self.words)

    def _create_model(self):

        histogram = self._create_histogram()
        markov_model = {}

        for key, value in histogram.items():
            temp_value = {}
            if key not in markov_model:
                temp_key = key
                for i in range(0, len(self.words)-1):
                    temp_word = self.words[i]
                    if temp_word == temp_key:
                        next_word = self.words[i + 1]
                        temp_value[next_word] = histogram.frequency(next_word)
            markov_model[key] = temp_value
        return markov_model

    def generate_sentence(self, num_of_characters):

        model = self._create_model()

        for key,value in model.items():

            #print(len(self.sentence))
            current_state = key
            if len(self.sentence) == 0:
                self.sentence = "{}".format(current_state)

            if len(value) == 0:
                self.sentence += key
                break

            if len(self.sentence) >= num_of_characters:
                return self.sentence

            for innerKey,innerValue in model.items():
                if innerKey == current_state and len(innerValue) != 0:
                    nested_word = dict_frequency_sample(innerValue)
                    self.sentence += " {} ".format(nested_word)

                elif len(innerValue) == 0:
                    pass
                current_state = nested_word

        return self.sentence
