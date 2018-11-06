from flask import Flask
import sys
sys.path.insert(0,"/Users/mediassumani/Documents/dev/cs/Courses/CS1.2/SectionTwo")
from dictionary_words import generateSentence
#from manage import Manage
#from dictionary_words import generateSentence
app = Flask(__name__)

@app.route('/')
def main_route():
    return generateSentence(10)
