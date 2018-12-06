from random import choice
from dictogram import Dictogram
from stochatic_sample import dict_frequency_sample
from file_opener import read_file


class Markov(dict):

    def __init__(self, word_list):
        super(Markov, self).__init__()
        self.order = 1
        self._create(words)

    def _create(self, words):

        words = tuple(words)
        for i in range(len(words) - self.order):
            current = words[i:i+self.order]
            next = words[i + self.order]

            if current not in self:
                self[current] = Dictogram()
            self[current].add_count(next)

    def random_walk(self, num_words=10):

        words = [*choice(list(self.keys()))]
        for _ in range(num_words - self.order):
            previous = tuple(words[-self.order:])
            words.append(self[previous].sample())

        return ' '.join(words)


def main():

    text_list = read_file("dummy.txt")
    chain = Markov(text_list)
    sentence = chain.random_walk()

if __name__ == '__main__':
    main()
