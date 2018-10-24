"""

To start, we'll be building a script that randomly rearranges a set of words provided as
command-line arguments to the script.For example, if you run the following command (assuming
 your script name is rearrange.py, though you can use any name you like)

$ python rearrange.py how now brown cow

You should see output like this: brown cow now how

"""
import random
import sys

def main():

    rearrange()

def rearrangeList():
""" Randomly prints a each elemnt from the commend line arguments """

    # storess the list of arguments passed into a new list, excluding the first elment(filename.py)
    list_of_argv =  sys.argv[1: len(sys.argv)]
    while len(list_of_argv) > 0:

        # Gets a random integer within range of 0 to the length of the list
        random_index = random.randint(0, len(list_of_argv) - 1)
        # Uses the list's pop method to randomly pop and print an element
        print(list_of_argv.pop(random_index))

if __name__ == "__main__":
    main()
