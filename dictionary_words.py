import sys
import os

def main():

    generate_sentence()

def generate_sentence():

    file_path = 'words'

    try:
        with open(file_path, 'r') as text_file:
            for line in text_file:
                print(line)

    except IOError:
        print("Error Found : Unable to find file")

if __name__ == "__main__":
    main()
