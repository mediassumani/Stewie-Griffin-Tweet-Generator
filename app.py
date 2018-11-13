
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

app = Flask(__name__)
file_path = 'stewi_griffin_scripts.txt'
text_body = read_file(file_path)

# Home Route
@app.route('/')
def index():
    return "Hello Medi"
