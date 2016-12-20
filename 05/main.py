from hashlib import md5
from re import compile


class DoorCodeCracker(object):
    @staticmethod
    def decryptInOrder(value, codeLength, match):
        prog = compile("^" + match + ".+$")
        currentCode = ""
        indexValue = 0
        while len(currentCode) < codeLength:
            currentValue = (value + str(indexValue)).encode("ascii")
            md5Hash = md5()
            md5Hash.update(currentValue)
            currentHash = md5Hash.hexdigest()
            if prog.match(currentHash):
                currentCode += currentHash[5]
                print("The current code is:", currentCode)
            indexValue += 1
        return currentCode

    @staticmethod
    def decryptWithPositions(value, codeLength, match):
        prog = compile("^" + match + ".+$")
        currentCode = [" "] * codeLength
        print(currentCode)
        indexValue = 0
        while " " in currentCode:
            currentValue = (value + str(indexValue)).encode("ascii")
            md5Hash = md5()
            md5Hash.update(currentValue)
            currentHash = md5Hash.hexdigest()
            if prog.match(currentHash):
                try:
                    changeIndex = int(currentHash[5])
                    if currentCode[changeIndex] == " ":
                        currentCode[changeIndex] = currentHash[6]
                        print(currentCode)
                except ValueError:
                    pass
                except IndexError:
                    pass
            indexValue += 1
        return "".join(currentCode)


def main():
    print("The code to the first door is:", DoorCodeCracker.decryptInOrder("abbhdwsy", 8, "00000"))
    print("The code to the second door is:", DoorCodeCracker.decryptWithPositions("abbhdwsy", 8, "00000"))

if __name__ == "__main__":
    main()
