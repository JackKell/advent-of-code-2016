from re import search


class DataLinkDecrypter(object):
    @staticmethod
    def decrypt(encryptedString):
        encryptedString = "".join(encryptedString.split())
        encrptedStringLength = len(encryptedString)
        decryptedString = ""
        currentIndex = 0
        while currentIndex < encrptedStringLength:
            currentChar = encryptedString[currentIndex]
            if currentChar != "(":
                decryptedString += currentChar
                currentIndex += 1
            else:
                endOfMarker = encryptedString.index(")", currentIndex)
                currentMarker = encryptedString[currentIndex:endOfMarker + 1]
                markerGroups = search(r"\((\d+)x(\d+)\)", currentMarker)
                if markerGroups:
                    offset = endOfMarker + 1
                    distance = int(markerGroups.group(1))
                    repeats = int(markerGroups.group(2))
                    repeatString = encryptedString[offset: offset + distance]
                    repatedStringLength = len(repeatString)
                    decryptedString += repeatString * repeats
                    change = len(currentMarker) + len(repeatString)
                    if repatedStringLength != distance:
                        raise ValueError
                    currentIndex += change
                else:
                    decryptedString += currentChar
                    currentIndex += 1
        return decryptedString


def main():
    with open("input.txt", "r") as inputFile:
        encryptedString = inputFile.read()
    decryptedString = DataLinkDecrypter.decrypt(encryptedString)
    print(len(decryptedString))

    # Tests
    # DataLinkDecrypter.decrypt("ADVENT")
    # DataLinkDecrypter.decrypt("A(1x5)BC")
    # DataLinkDecrypter.decrypt("(3x3)XYZ")
    # DataLinkDecrypter.decrypt("A(2x2)BCD(2x2)EFG")
    # DataLinkDecrypter.decrypt("(6x1)(1x3)A")
    # DataLinkDecrypter.decrypt("X(8x2)(3x3)ABCY")
    # DataLinkDecrypter.decrypt("(3x3)ABC")
    # DataLinkDecrypter.decrypt("(3x10)ABC")


if __name__ == '__main__':
    main()
