class Taxi(object):
    def __init__(self, startPoint=[0, 0]):
        self.direction = 0
        self.startPoint = startPoint
        self.currentPoint = startPoint[:]
        self.history = [tuple(startPoint)]

    @property
    def distanceToStart(self):
        return self.getDistanceFromPoint(self.startPoint, self.currentPoint)

    @property
    def distanceToFirstRevisitedPoint(self):
        firstRevistedPoint = self.getFirstRevistedPoint()
        print(firstRevistedPoint)
        if (firstRevistedPoint):
            return self.getDistanceFromPoint(firstRevistedPoint, self.currentPoint)
        return None

    def getDistanceFromPoint(self, startPoint, endPoint):
        return sum([abs(starti - endi) for starti, endi in zip(startPoint, endPoint)])

    def turn(self, turnChar):
        if turnChar == "L":
            self.direction += 3
        elif turnChar == "R":
            self.direction += 1
        self.direction %= 4

    def move(self):
        if self.direction == 0:
            self.currentPoint[1] += 1
        elif self.direction == 1:
            self.currentPoint[0] += 1
        elif self.direction == 2:
            self.currentPoint[1] -= 1
        elif self.direction == 3:
            self.currentPoint[0] -= 1

    def processInstruction(self, instruction):
        turnChar = instruction[0]
        distance = int(instruction[1:])
        self.turn(turnChar)
        for i in range(0, distance):
            self.move()
            self.history.append(tuple(self.currentPoint))

    def getFirstRevistedPoint(self):
        for i in range(1, len(self.history)):
            currentLocation = self.history[i]
            if currentLocation in self.history[:i]:
                return currentLocation
        return None

    def printRevistedPoints(self):
        revistedPoints = []
        for i in range(1, len(self.history)):
            currentLocation = self.history[i]
            if currentLocation in self.history[:i]:
                revistedPoints.append(currentLocation)
        print(revistedPoints)


def main():
    with open("input", "r") as inputFile:
        instructions = inputFile.read().split(", ")
    taxi = Taxi()
    for instruction in instructions:
        taxi.processInstruction(instruction)
    print(taxi.history)
    print("distance to start:", taxi.distanceToStart)
    print("distance to first revisited point:", taxi.distanceToFirstRevisitedPoint)
    taxi.printRevistedPoints()


if __name__ == '__main__':
    main()
