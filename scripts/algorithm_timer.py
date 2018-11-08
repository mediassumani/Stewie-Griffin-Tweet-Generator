# Module contains a wrapper method to benchmark my algorithm performance
# Implemented by Medi A.

import time

def timing_function(function_parameter):
    """
    This Function outputs the time it takes to execute a function
    """
    def wrapper():
        starting_time = time.time()
        function_parameter()
        ending_time = time.time()

        return "\nIt took : {} seconds to execute\n".format(str(ending_time - starting_time))
    return wrapper
