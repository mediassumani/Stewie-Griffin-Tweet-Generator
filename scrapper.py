import sys
import re
import os
import requests
from file_opener import read_file
from bs4 import BeautifulSoup


def download_data(url):
    """ Downloads the data from the URL"""

    request = requests.get(url)
    status_code = request.status_code
    data = request.text

    return data

def clean_up_data(data):
    """ Cleans up an web page of HTML tags and unwanted characters"""

    soup = BeautifulSoup(data, "html.parser")
    clean_up_data = soup.find("div", "scrolling-script-container").text.strip()

    return clean_up_data

def find_stewie_scripts(data):

    pass


def write_in_file(data):
    """ Writes the cleaned up data into an internal text file"""
    pass

def main():

    url = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=family-guy&episode=s01e02"
    data = download_data(url)
    cleaned_split_data = clean_up_data(data).split()
    sentence = []
    starting_index = 0
    ending_index = 0
    indexes = []


    mock_text = ["the", "boy","STEWIE:","what","the","deuce","PETER:", "hi", "STEWIE", "is", "STEWIE:", "get", "that", "bloody", "love"]
    for index, word in enumerate(cleaned_split_data):
        if word == "STEWIE:":
            starting_index = index + 1
            indexes.append(starting_index)

        if word[-1:] == ":" and word != "STEWIE:" :
            ending_index = index - 1
            indexes.append(ending_index)


        try:
            if mock_text[index+1]:
                pass
        except IndexError:
            indexes.append(index+1)

    counter = 0
    step = 0
    while counter < len(indexes):

        try:
            sentence.append(mock_text[indexes[step]:indexes[step+1]])
            sentence.append([mock_text[indexes[step+1]]])
            counter += 1
            step += 2

        except IndexError:
            break
            last_index = indexes[step-1]
            sentence.append(mock_text[indexes[step-2]:indexes[step-1]])


    print(sentence)


if __name__ == "__main__":
    main()
