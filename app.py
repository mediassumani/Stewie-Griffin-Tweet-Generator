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


for key,value in histogram.items():
    temp_value = []
    if key not in markov_model:
        temp_key = key
        for i in range(0, len(text_list)-1):
            if text_list[i] == temp_key:
                temp_value.append(text_list[i + 1])

    markov_model[key] = temp_value


for key,value in markov_model.items():
    if len(sentence) == 0:
        sentence = "{} ".format(key)

    elif len(value) == 0:
        sentence += key
        break

    else:
        random_index = randint(0, len(value)-1)
        random_choice = value[random_index]
        sentence += random_choice
        for innerKey,innerValue in markov_model.items():
            if innerKey == random_choice and innerKey != "STOP":
                rand_index = randint(0, len(innerValue)-1)
                sentence += " {} ".format(innerValue[rand_index])
                break


# for key, value in markov_model.items():
#     if len(value) == 0:
#         break
#     elif "STOP" in value:
#         break
#     else:
#         random_index = random.randint(0, len(value)-1)
#         sentence += " {}".format(value[random_index])
    # there's an empty list, figure it out!!!
print(markov_model)
print("\n\n Sentence generated : {} \n\n".format(sentence))
