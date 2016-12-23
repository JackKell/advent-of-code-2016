class BotFactory(object):
    def __init__(self):
        self.botLookup = dict()
        self.output = []

    def addBot(self):
        pass


class Bot(object):
    def __init__(self, id, low=None, high=None, botLookup):
        self.microChip = None
        self.id = id
        self.botLookup = botLookup
        self.low = low
        self.high = high

    def addMicroChip(self, number):
        pass

def main():
    pass

if __name__ == '__main__':
    main()
