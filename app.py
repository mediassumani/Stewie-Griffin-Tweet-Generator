
"""
FILENAME:               app.py
AUTHOR:                 Medi Assumani
DESCRIPTION:            Entry point of the Stswie Griffin Tweet Generator that containts
                        the flask server and connected with needed internal modules.
"""



from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_route():
    return "Hello Medi"
