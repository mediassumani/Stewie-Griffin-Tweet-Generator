from random import choice
from stochatic_sample import dict_frequency_sample

class Markov(dict):
    """ Represents a 2nd order markov model """

    def __init__(self,word_list=None):
        """ Initializes the object with a list of tokenized words"""
        super(Markov,self).__init__()
        self.words = word_list
        if word_list is not None:
            size = len(word_list)-2

            for index in range(0, size):
                tuple_pair_of_words = (word_list[index],word_list[index+1]) #stores the first two word
                next_word = word_list[index+2] # stores the third word
                self._create_model(tuple_pair_of_words,next_word)

    def _create_model(self,word_tuple,next_word):
        """ Creates the markov model of 2nd order
            @param - word_tuple: a tuple that contains the previous word and generated word
            @param - next_word: the word tha comes after the second element of the word_tuple
        """

        if word_tuple in self:

            if next_word in self[word_tuple]:
                # increments the frequency of next word if it's seen before
                self[word_tuple][next_word] += 1
            else:
                # assigns a value of 1 if the next word is never seen
                self[word_tuple][next_word] = 1
        else:
            # assigns a new tuple entry in the histogram if
            self[word_tuple] = {next_word:1}

    def random_walk(self, length):
        """ Returns  a sentence based on its word freqencies
            @param - length: the amount of words for the sentence
            @return - the sentence generated
        """

        sentence = []
        markov_model = Markov(self.words)

        if len(markov_model) == 0:
            print("Error Found: Empty histogram")

        weighted_word = choice(list(markov_model.keys()))

        while len(sentence) != length:
            sentence .append(weighted_word[1])
            weighted_word = (weighted_word[1], dict_frequency_sample(markov_model[weighted_word]))

        return " ".join(sentence) + "."
