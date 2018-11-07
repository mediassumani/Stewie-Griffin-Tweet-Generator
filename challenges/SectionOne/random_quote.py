import random

# some random quotes from stweie griffin
quotes = ["You even cried after Columbine",
          "Ehh... it was kind of a regional tragedy",
          "I just realized something. Tomorrow is Sunday",
         "Come on, it's throw up. You like throw up",
         "Hey, let's, you know, let's have an underpants party,"]

def random_python_quote():
    random_index = random.randint(0, len(quotes) - 1)
    return quotes[random_index]

def main():
    generated_quote = random_python_quote()
    print generated_quote

if __name__ == '__main__':
    main()
