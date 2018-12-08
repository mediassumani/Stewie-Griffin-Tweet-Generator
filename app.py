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
from markov import Markov

app = Flask(__name__)

# Route : Index
@app.route('/')
def index():

    text_list = read_file("stewi_griffin_scripts.txt")
    markov_model = Markov(text_list)

    return markov_model.generate_sentence(200)
