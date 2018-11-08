"""

To start, we'll be building a script that randomly rearranges a set of words provided as
command-line arguments to the script.For example, if you run the following command (assuming
 your script name is rearrange.py, though you can use any name you like)

$ python rearrange.py how now brown cow

You should see output like this: brown cow now how

"""
import sys
import random
from algorithm_timer import timing_function

def rearrange_list():

    # stores the list of arguments passed into a new list, excluding the first elment(filename.py)
    list_of_argv =  sys.argv[1:]
    result = []
    while len(list_of_argv) > 0:

        # Gets a random integer within range of 0 to the length of the list
        random_index = random.randint(len(list_of_argv) - 1)
        # Uses the list's pop method to randomly pop and print an element
        result.append(list_of_argv.pop(random_index))

    return result

@timing_function
def tester():
    print(rearrange_list())
print(tester())


if __name__ == "__tester__":
    tester()
