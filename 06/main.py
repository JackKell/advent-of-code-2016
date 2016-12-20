from collections import Counter
from enum import Enum


class DecodeMethod(Enum):
    MOST_COMMON = 0
    LEAST_COMMON = 1


class AntiJammer(object):
    @staticmethod
    def decode(partials, decodeMethod=DecodeMethod.MOST_COMMON):
        # Merge all the partials by index into basically a list with each element
        # being string of values at a given index of the partial
        partialSize = len(partials[0])
        listByIndex = [""] * partialSize
        for partial in partials:
            for i in range(0, partialSize):
                listByIndex[i] += (partial[i])

        # Counter to find the most common or least common value at each index
        for i in range(0, partialSize):
            if decodeMethod == DecodeMethod.MOST_COMMON:
                listByIndex[i] = Counter(listByIndex[i]).most_common(1)[0][0]
            elif decodeMethod == DecodeMethod.LEAST_COMMON:
                listByIndex[i] = Counter(listByIndex[i]).most_common()[-1:][0][0]
            else:
                raise ValueError

        # Convert the list to a string
        return "".join(listByIndex)


def main():
    with open("inputTest.txt", "r") as inputFile:
        partials = inputFile.read().splitlines()

    print("The unjammed message for the test data is (Most common):", AntiJammer.decode(partials))
    print("The unjammed message for the test data is (Least common:", AntiJammer.decode(partials, DecodeMethod.LEAST_COMMON))

    with open("input.txt", "r") as inputFile:
        partials = inputFile.read().splitlines()

    print("The unjammed message for the data is (Most common):", AntiJammer.decode(partials))
    print("The unjammed message for the data is (Least common:", AntiJammer.decode(partials, DecodeMethod.LEAST_COMMON))

if __name__ == "__main__":
    main()
