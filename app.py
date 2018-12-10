"""
FILENAME:               app.py
AUTHOR:                 Medi Assumani
DESCRIPTION:            Entry point of the Stewie Griffin Tweet Generator that containts
                        the flask server and connected with needed internal modules.
"""

from flask import Flask
from file_opener import read_file
from stochatic_sample import dict_frequency_sample
from markov import Markov

app = Flask(__name__)

@app.route('/')
def index():

    text_list = read_file("stewi_griffin_scripts.txt")
    markov_model = Markov(text_list)
    print(len(text_list))
    return  markov_model.random_walk(30)
