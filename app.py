"""
FILENAME:               app.py
AUTHOR:                 Medi Assumani
DESCRIPTION:            Entry point of the Stewie Griffin Tweet Generator that containts
                        the flask server and connected with needed internal modules.
"""

from flask import Flask, render_template
from file_opener import read_file
from stochatic_sample import dict_frequency_sample
from markov import Markov
from clean_up import clean

app = Flask(__name__)

@app.route('/')
def index():

    text_list = read_file("stewi_griffin_scripts.txt")
    markov_model = Markov(text_list)
    return  render_template("home.html", sentence= markov_model.random_walk(15))
