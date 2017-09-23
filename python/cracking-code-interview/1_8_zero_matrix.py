# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
import unittest

def build_new_matrix(m, n):
    matrix = []
    for i in range(m):
        sub_matrix = []
        for j in range(n):
            sub_matrix.append('')
        matrix.append(sub_matrix)
    return matrix


def zero_matrix(matrix, m, n):
    rows = set()
    columns = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "0":
                rows.add(i)
                columns.add(j)

    for i in rows:
        for j in range(n):
            matrix[i][j] = "0"

    for i in columns:
        for j in range(m):
            matrix[j][i] = "0"


def matrix_to_text(matrix):
    text = "    0   1   2   3\n"
    for i in range(len(matrix)):
        text += str(i) + " | "
        for j in matrix[i]:
            text += j + " | "
        text += "\n"
    return text


class TestFunctions(unittest.TestCase):
    def testRotate(self):

        source = [
            [' ', ' ', ' ', ' '],
            [' ', '0', ' ', ' '],
            [' ', ' ', '0', ' '],
            [' ', ' ', ' ', ' ']
        ]

        print(matrix_to_text(source))

        print("-----------------------------------------\n")
        zero_matrix(source, 4, 4)
        print("\n-----------------------------------------")

        expected = [
            [' ', '0', '0', ' '],
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0'],
            [' ', '0', '0', ' ']
        ]

        print(matrix_to_text(source))
