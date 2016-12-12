class KeyPadSolver(object):
    def __init__(self, keypad, startPosition):
        self.__keypad = keypad
        self.__startPosition = startPosition[:]
        self.__currentPosition = startPosition[:]

    def __getNumber(self, instruction):
        for letter in instruction:
            if letter == "U":
                newY = self.__currentPosition[1] - 1
                if newY >= 0:
                    nextValue = self.__keypad[newY][self.__currentPosition[0]]
                    if nextValue:
                        self.__currentPosition[1] = newY
            elif letter == "R":
                newX = self.__currentPosition[0] + 1
                if newX < len(self.__keypad[0]):
                    nextValue = self.__keypad[self.__currentPosition[1]][newX]
                    if nextValue:
                        self.__currentPosition[0] = newX
            elif letter == "D":
                newY = self.__currentPosition[1] + 1
                if newY < len(self.__keypad):
                    nextValue = self.__keypad[newY][self.__currentPosition[0]]
                    if nextValue:
                        self.__currentPosition[1] = newY
            elif letter == "L":
                newX = self.__currentPosition[0] - 1
                if newX >= 0:
                    nextValue = self.__keypad[self.__currentPosition[1]][newX]
                    if nextValue:
                        self.__currentPosition[0] = newX
            else:
                raise ValueError("Bad letter ,\"", letter, "\" in given code!")
        return self.__keypad[self.__currentPosition[1]][self.__currentPosition[0]]

    def getCode(self, instructions):
        code = ""
        for instruction in instructions:
            value = self.__getNumber(instruction)
            code += str(value)
        self.__currentPosition = self.__startPosition[:]
        return code


def main():
    with open("input", "r") as inputFile:
        instructions = inputFile.read().splitlines()

    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    startPos = [1, 1]
    keyPadSolver = KeyPadSolver(keypad, startPos)
    code = keyPadSolver.getCode(instructions)
    print("Code 1:", code)

    keypad = [[None, None, 1, None, None],
              [None, 2, 3, 4, None],
              [5, 6, 7, 8, 9],
              [None, "A", "B", "C", None],
              [None, None, "D", None, None]]
    startPos = [0, 2]
    keyPadSolver = KeyPadSolver(keypad, startPos)
    code = keyPadSolver.getCode(instructions)
    print("Code 2:", code)

if __name__ == '__main__':
    main()
