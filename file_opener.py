
def read_file(file_path):
    """Returns a body of text read from a text file
       @param - file_name : the soure file to read from
       @return - file_content : The body of the text file
    """

    try:
        with open(file_path, 'r') as file:
            return file.read().split()
    except IOError:
        print("Error: FILE NOT FOUND")
