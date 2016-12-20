from itertools import permutations


class TriangleChecker(object):
    @staticmethod
    def isValidTriangle(triangle):
        if len(triangle) != 3:
            raise ValueError
        for currentSet in permutations(triangle, 3):
            if currentSet[0] + currentSet[1] <= currentSet[2]:
                return False
        return True

    @staticmethod
    def validTriangleCount(triangles):
        count = 0
        for triangle in triangles:
            isValidTraingle = TriangleChecker.isValidTriangle(triangle)
            if isValidTraingle:
                count += 1
        return count


def main():
    with open("input", "r") as inputFile:
        wallInput = inputFile.read()

    # in the input file make each row a triangle
    trianglesAsRows = [list(map(int, i.split())) for i in wallInput.splitlines()]
    print("Number of valid triangles:", TriangleChecker.validTriangleCount(trianglesAsRows))

    # in the input file make each row a triangle
    columns = [list(col) for col in zip(*trianglesAsRows)]

    # flatten the list
    series = sum(columns, [])

    # make each vertical set of 3 into a triangle
    trianglesByColumn = [series[x:x+3] for x in range(0, len(series), 3)]

    print("Number of valid triangles:", TriangleChecker.validTriangleCount(trianglesByColumn))

if __name__ == '__main__':
    main()
