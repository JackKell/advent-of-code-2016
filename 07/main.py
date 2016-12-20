from re import compile
from re import match

class IpSevenAddress(object):
    def __init__(self, address):
        self.address = address

    def supportsTSL(self):
        prop = compile(".*((.)([^\3])\3\2)(?![^\[]*\]).*")
        results = match(".*((.)([^\3])\3\2)(?![^\[]*\]).*", self.address)
        print(results)

def main():
    with open("inputTest.txt", "r") as inputFile:
        ipAddresses = inputFile.read().splitlines()

    print(ipAddresses)
    for ipAddress in ipAddresses:
        addr = IpSevenAddress(ipAddress)
        addr.supportsTSL()


if __name__ == "__main__":
    main()

# contine work on the regex at https://regex101.com/delete/FBxSy1Df4n2FYqzHRYQPhi1U
