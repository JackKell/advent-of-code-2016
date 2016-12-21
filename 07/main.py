from re import compile
from re import search


class IpSevenAddress(object):
    def __init__(self, address):
        # TODO: find a way to make this a static variable
        self.tslPattern = compile(r".*((.)(?!\2)(.)\3\2).*")
        self.address = address
        nets = self.address.replace("]", "[").split("[")
        self.hypernets = nets[1::2]
        self.supernets = nets[::2]

    @property
    def supportsTSL(self):
        tslPatternInNonHyperNet = False
        for nonHypernet in self.supernets:
            if bool(self.tslPattern.match(nonHypernet)):
                tslPatternInNonHyperNet = True
                break

        tslPatternInHyperNet = False
        for hypernet in self.hypernets:
            if bool(self.tslPattern.match(hypernet)):
                tslPatternInHyperNet = True
                break

        return tslPatternInNonHyperNet and not tslPatternInHyperNet

    @property
    def supportsSSL(self):
        possibleABAs = []
        possibleBABs = []
        for supernet in self.supernets:
            for i in range(0, len(supernet) - 2):
                first = supernet[i]
                second = supernet[i+1]
                third = supernet[i+2]
                if first != second and first == third:
                    possibleABAs.append(first + second + third)

        for aba in possibleABAs:
            first = aba[1]
            second = aba[0]
            possibleBABs.append(first + second + first)

        # print(possibleABAs)
        # print(possibleBABs)

        for hypernet in self.hypernets:
            for bab in possibleBABs:
                if bab in hypernet:
                    return True

def main():
    with open("input.txt", "r") as inputFile:
        ipAddresses = inputFile.read().splitlines()

    tslSupportCount = 0
    sslSupportCount = 0
    for ipAddress in ipAddresses:
        currentAddress = IpSevenAddress(ipAddress)
        if currentAddress.supportsTSL:
            tslSupportCount += 1
        if currentAddress.supportsSSL:
            print(ipAddress)
            sslSupportCount += 1

    print(tslSupportCount, "out of the", len(ipAddresses), "given addresses support tsl")
    print(sslSupportCount, "out of the", len(ipAddresses), "given addresses support ssl")


if __name__ == "__main__":
    main()
