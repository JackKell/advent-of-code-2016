from re import search
from collections import Counter


class RoomCode(object):
    def __init__(self, rawCode):
        self.code = rawCode
        regexResults = search("^(.+)-(\d+)\[(.+)\]$", rawCode)
        self.data = regexResults.group(1)
        self.id = int(regexResults.group(2))
        self.checkSum = regexResults.group(3)

    def __str__(self):
        return self.code

    def __repr__(self):
        return self.code

    def isRealRoomCode(self):
        charCount = Counter(self.data.replace("-", ""))
        # don't understand how this works XD but it sorts the
        # charCount dictionary by frequency and then alphabetically
        # still confused by the lambda though
        # http://stackoverflow.com/questions/16006630/how-to-organize-list-by-frequency-of-occurrence-and-alphabetically-in-case-of-a
        mostCommonChars = sorted(charCount, key=lambda char: (-charCount[char], char))
        for i in range(0, len(self.checkSum)):
            ithMostCommonChar = mostCommonChars[i]
            if ithMostCommonChar != self.checkSum[i]:
                return False
        return True

    @staticmethod
    def shiftString(value, amount=0):
        shitftedValue = ""
        for character in value:
            characterCode = ord(character)
            if characterCode in range(97, 123):
                shitftedValue += chr(((characterCode - (97 - amount)) % 26) + 97)
            else:
                shitftedValue += " "
        return shitftedValue

    def decrypt(self):
        return RoomCode.shiftString(self.data, self.id)


def main():
    with open("input.txt", "r") as inputFile:
        instructions = inputFile.read().splitlines()

    validRoomCodes = []
    for instruction in instructions:
        currentRoomCode = RoomCode(instruction)
        if currentRoomCode.isRealRoomCode():
            validRoomCodes.append(currentRoomCode)
    roomIDSum = 0
    for roomCode in validRoomCodes:
        roomIDSum += roomCode.id
    print("Sum of valid room IDs:", roomIDSum)

    for roomCode in validRoomCodes:
        if roomCode.decrypt() == "northpole object storage":
            print("Northpole object storage room number:", roomCode.id)
            break

if __name__ == '__main__':
    main()
