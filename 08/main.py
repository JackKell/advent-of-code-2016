from re import compile
from collections import deque
import os
from time import sleep


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class LCDScreen(object):
    # size (x, y)
    # self.screen[rowIndex][columnIndex]
    def __init__(self, size, offSymbol=".", onSymbol="#"):
        self.instructionPattern = compile(r"(rect|rotate)\s((\d+)x(\d+)|row|column)?\s?(?:(?:x|y)=(\d+) by (\d+))?")
        self.offSymbol = offSymbol
        self.onSymbol = onSymbol
        self.screen = [[offSymbol for x in range(size[0])] for y in range(size[1])]

    def processInstruction(self, instruction):
        instructionGroups = self.instructionPattern.search(instruction)
        if instructionGroups.group(1) == "rect":
            self.rect([int(instructionGroups.group(3)), int(instructionGroups.group(4))])
        if instructionGroups.group(1) == "rotate":
            self.rotate(instructionGroups.group(2),
                        int(instructionGroups.group(5)),
                        int(instructionGroups.group(6)))

    def display(self):
        print()
        for row in self.screen:
            print("".join(row))

    def rect(self, size):
        count = 0
        for rowIndex in range(0, size[1]):
            for columnIndex in range(0, size[0]):
                count += 1
                self.screen[rowIndex][columnIndex] = self.onSymbol

    def rotate(self, axis, index, distance):
        if axis in ["row", 0, "x"]:
            rotatedRow = self.__rotateList(self.getRow(index), distance)
            self.setRow(index, rotatedRow)
        elif axis in ["column", 1, "y"]:
            rotatedColumn = self.__rotateList(self.getColumn(index), distance)
            self.setColumn(index, rotatedColumn)
        else:
            raise ValueError

    @property
    def activePixelCount(self):
        activePixelCount = 0
        for row in self.screen:
            for pixel in row:
                if pixel == "#":
                    activePixelCount += 1
        return activePixelCount

    @property
    def size(self):
        y = len(self.screen)
        x = len(self.screen[0])
        return tuple((x, y))

    @staticmethod
    def __rotateList(inputList, distance):
        rotatedList = deque(inputList)
        rotatedList.rotate(distance)
        return list(rotatedList)

    def getRow(self, rowIndex):
        return self.screen[rowIndex]

    def setRow(self, rowIndex, newRow):
        if len(newRow) != self.size[0]:
            raise ValueError
        self.screen[rowIndex] = newRow

    def getColumn(self, columnIndex):
        column = []
        for rowIndex in range(0, self.size[1]):
            for pixel in self.screen[rowIndex][columnIndex]:
                column.append(pixel)
        return column

    def setColumn(self, columnIndex, newColumn):
        if len(newColumn) != self.size[1]:
            raise ValueError
        for rowIndex in range(0, self.size[1]):
            self.screen[rowIndex][columnIndex] = newColumn[rowIndex]


def main():
    testScreen = LCDScreen([7, 3])
    testScreen.display()
    testScreen.processInstruction("rect 3x2")
    testScreen.display()
    testScreen.processInstruction("rotate column x=1 by 1")
    testScreen.display()
    testScreen.processInstruction("rotate row y=0 by 4")
    testScreen.display()
    testScreen.processInstruction("rotate column x=1 by 1")
    testScreen.display()

    clear()

    screen = LCDScreen([50, 6])
    screen.display()
    with open("input.txt", "r") as inputFile:
        instructions = inputFile.read().splitlines()

    for instruction in instructions:
        clear()
        screen.processInstruction(instruction)
        screen.display()
        sleep(0.05)

    clear()
    screen.display()
    print("This number of active pixels is:", screen.activePixelCount)


if __name__ == "__main__":
    main()
