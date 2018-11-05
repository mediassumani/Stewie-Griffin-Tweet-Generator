from flask import Flask
from manage import Manage
#from dictionary_words import generateSentence
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world'
