"""
FILENAME:               app.py
AUTHOR:                 Medi Assumani
DESCRIPTION:            Entry point of the Stswie Griffin Tweet Generator that containts
                        the flask server and connected with needed internal modules.
"""

from flask import Flask
import sys
from random import randint
from file_opener import read_file
from histogram_generator import generate_histogram
from sentence import generate_sentence
from stochatic_sample import dict_frequency_sample

app = Flask(__name__)

# Route : Index
@app.route('/')
def index():
    # file_path = 'stewi_griffin_scripts.txt'
    # text = read_file(file_path)
    # histogram = generate_histogram(text)
    #
    # return generate_sentence(histogram, 10)
    return "I am amazing!"

markov_model = {}
text_list = read_file("dummy.txt")
histogram = generate_histogram(text_list)
sentence = ""

for key, value in histogram.items():
    temp_value = {}
    if key not in markov_model:
        temp_key = key
        for i in range(0, len(text_list)-1):
            temp_word = text_list[i]
            if temp_word == temp_key:
                next_word = text_list[i + 1]
                temp_value[next_word] = histogram.frequency(next_word)
    markov_model[key] = temp_value

for key,value in markov_model.items():
    current_state = key
    if len(sentence) == 0:
        sentence = "{}".format(current_state)
    # selected_word = dict_frequency_sample(value)
    # sentence += selected_word

    if len(value) == 0:
        sentence += key
        break
    for innerKey,innerValue in markov_model.items():
        if innerKey == current_state:
            nested_word = dict_frequency_sample(innerValue)
            sentence += " {} ".format(nested_word)

        elif len(innerValue) == 0:
            pass
            #sentence += innerKey
        current_state = nested_word

    # else:
        # selected_word = dict_frequency_sample(value)
        # sentence += selected_word
        # print(key,value)
        # for innerKey,innerValue in markov_model.items():
        #     if len(innerValue) == 0:
        #         break
        #     if innerKey == selected_word:
        #         sentence += " {} ".format(dict_frequency_sample(innerValue))
        #         break



print(markov_model)
print("\n\nsentence generated : {} \n".format(sentence))
