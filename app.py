"""
FILENAME:               app.py
AUTHOR:                 Medi Assumani
DESCRIPTION:            Entry point of the Stswie Griffin Tweet Generator that containts
                        the flask server and connected with needed internal modules.
"""

from flask import Flask
import sys
sys.path.insert(0,'./scripts')
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

dict_of_dict = {}

text_list = read_file("fish.txt")
histogram = generate_histogram(text_list)


for key,value in histogram.items():
    temp_value = []
    if key not in dict_of_dict:
        temp_key = key

        # for index, word in enumerate(text_list):
        for i in range(0, len(text_list)-1):
            if text_list[i] == temp_key:
                temp_value.append(text_list[i + 1])

            # if text_list[i+1] is not None:
            #     temp_value.append(text_list[i+1])
                # dict_of_dict[key] += temp_value

    dict_of_dict[key] = temp_value
print(dict_of_dict)
