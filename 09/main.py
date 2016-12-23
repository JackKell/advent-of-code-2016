from time import time


class DataLinkDecompressor(object):
    @staticmethod
    def decompressedLength(encrptedString, version2=False, isStart=True):
        decompressedLength = 0
        currentIndex = 0
        while currentIndex < len(encrptedString):
            if isStart:
                print(round(((currentIndex + 1) / len(encrptedString)) * 100, 2), "% decompressed")
            if "(" not in encrptedString[currentIndex:]:
                decompressedLength += len(encrptedString[currentIndex:])
                return decompressedLength
            elif encrptedString[currentIndex] == "(":
                endOfMarker = encrptedString.index(")", currentIndex)
                subStringLength, repeats = map(int, (encrptedString[currentIndex + 1: endOfMarker]).split("x"))
                nextCurrentIndex = endOfMarker + subStringLength + 1
                if version2:
                    subString = encrptedString[endOfMarker + 1: nextCurrentIndex] * repeats
                    del subStringLength, repeats, endOfMarker
                    decompressedLength += DataLinkDecompressor.decompressedLength(subString, version2=True, isStart=False)
                else:
                    decompressedLength += subStringLength * repeats
                currentIndex = nextCurrentIndex
            else:
                decompressedLength += 1
                currentIndex += 1
        return decompressedLength



def main():
    with open("input.txt", "r") as inputFile:
        encryptedString = "".join(inputFile.read().split())
    # decryptedString = DataLinkDecrypter.decrypt(encryptedString)
    # print(len(decryptedString))

    v1tests = ["ADVENT", "A(1x5)BC", "(3x3)XYZ", "A(2x2)BCD(2x2)EFG",
             "(6x1)(1x3)A", "X(8x2)(3x3)ABCY", "(3x3)ABC", "(3x10)ABC"]
    print("Version 1")
    # for test in v1tests:
    #     print(test, DataLinkDecompressor.decompressedLength(test))

    print()

    print("Version 2")
    tests = ["(3x3)XYZ", "X(8x2)(3x3)ABCY", "(27x12)(20x12)(13x14)(7x10)(1x12)A",
             "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"]
    for test in tests:
        start = time()
        print(test, DataLinkDecompressor.decompressedLength(test, version2=True), round(time() - start, 10))
    start = time()

    # This takes 10 minutes to find the decompressed length
    # TODO: find a way to make this FASTER PLS
    # print(DataLinkDecompressor.decompressedLength(encryptedString, version2=True), round(time() - start, 3))


if __name__ == '__main__':
    main()
