import random

def sample_by_frequency(histogram):
    """ Returns a random word based on its weight"""
    accumulator = 0
    total_tokens = 0
    for list in histogram:
        total_tokens += list[1]

    random_integer = random.randint(1,total_tokens)

    for list in histogram:
        accumulator += list[1]
        if accumulator >= random_integer:
            return list[0]

def main():
    histogram_list = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
    tester_histogram = []
    for _ in range(0,10000):
        tester_histogram.append(sample_by_frequency(histogram_list))

    print("Word Fish is seen {} times".format(tester_histogram.count("fish")))
    print("Word One is seen {} times".format(tester_histogram.count("one")))
    print("Word Two is seen {} times".format(tester_histogram.count("two")))
    print("Word Red is seen {} times".format(tester_histogram.count("red")))
    print("Word Blue is seen {} times".format(tester_histogram.count("blue")))

if __name__ == "__main__":
    main()
