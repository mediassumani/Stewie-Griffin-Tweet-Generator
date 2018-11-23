""" Module for generation an histogram"""
import sys
sys.path.insert(0,'./scripts')
from dictogram import Dictogram

def generate_histogram(body_text):
    """  Returns a list histogram given a text"""
    return Dictogram(body_text)


if __name__ == "__main__":
    print(histogram('fish.txt'))
