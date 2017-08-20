# 1.7 Rotate Matrix

class MatrixClass:
    def __init__(self, rows, cols):
        self.numRows = rows
        self.numCols = cols

        # Create an empty matrix
        self.matrix = []
        for i in range(self.numRows):
            self.matrix.append([])
            for j in range(self.numCols):
                self.matrix[i].append([])

        print("Num Rows: " + str(len(self.matrix)))
        print("Num Cols: " + str(len(self.matrix[0])))


    def initializeMatrix(self):

        value = 0
        for i in range(self.numRows):
            for j in range(self.numCols):
                value += 1
                self.matrix[i][j] = value

    def printMatrix(self):

        for i in range(self.numRows):
            print(self.matrix[i])
        print("\n")

    def flipMatrix(self):

        for i in range(self.numRows):
            for j in range(i, self.numCols):
                cell = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[j][i]
                self.matrix[j][i] = cell

    def swapMatrix(self):
        for j in range(int(self.numCols / 2)):

            for i in range(self.numRows):
                cell = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[i][(self.numCols - 1) - j]
                self.matrix[i][(self.numCols - 1) - j] = cell

newMatrix = MatrixClass(4,4)
newMatrix.initializeMatrix()
newMatrix.printMatrix()

newMatrix.flipMatrix()
newMatrix.printMatrix()

newMatrix.swapMatrix()
newMatrix.printMatrix()
