import random

def sample_by_frequency(histogram):
    accumulator = 0
    random_integer = random.randint(1,histogram[-1][1])

    # for index, list in enumerate(histogram):
    #     accumulator += list[1]
    #     if accumulator >= random_integer:
    #         return list[0]
    return histogram[-1][1]


def main():
    histogram_list = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
    print(sample_by_frequency(histogram_list))

if __name__ == "__main__":
    main()
