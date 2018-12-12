import re
import string

def clean_up(text_body):
    """ Cleans up the text and lower cases every word
        @param - text_body - the string that needs to be cleaned
    """

    split_texts = text_body.split()
    clean_up_data = [word.lower().translate(None, string.punctuation) for word in split_texts]

    return clean_up_data

def read_file(file_path):
    """Returns a body of text read from a text file
       @param - file_name : the soure file to read from
       @return - file_content : The body of the text file
    """

    try:
        with open(file_path, 'r') as file:
            return clean_up(file.read())
    except IOError:
        print("Error: FILE NOT FOUND")
