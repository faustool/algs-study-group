import unittest


def build_new_matrix(length):
    matrix = []
    for i in range(length):
        sub_matrix = []
        for j in range(length):
            sub_matrix.append('')
        matrix.append(sub_matrix)
    return matrix


def rotate_matrix(matrix):
    step = 1
    for from_i in range(len(matrix)):
        for from_j in range(len(matrix[from_i])):
            to_i = from_j
            to_j = len(matrix) - from_i - 1
            debug_step(step, matrix, from_i, from_j, to_i, to_j)
            current = matrix[to_i][to_j]
            matrix[to_i][to_j] = matrix[from_i][from_j]
            matrix[from_i][from_j] = current
            step += 1
            print(matrix_to_text(matrix))


def debug_step(step, matrix, from_i, from_j, to_i, to_j):
    print("Step: " + str(step) +
          ", from[" + str(from_i) + "," + str(from_j) + "](" + matrix[from_i][from_j] + ")" +
          ", to[" + str(to_i) + "," + str(to_j) + "](" + matrix[to_i][to_j] + ")")


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
            [' ', 'x', ' ', ' '],
            [' ', 'x', 'x', ' '],
            [' ', ' ', 'x', ' '],
            [' ', ' ', ' ', ' ']
        ]

        print(matrix_to_text(source))

        print("-----------------------------------------\n")
        rotate_matrix(source)
        print("\n-----------------------------------------")

        expected = [
            [' ', ' ', ' ', ' '],
            [' ', ' ', 'x', 'x'],
            [' ', 'x', 'x', ' '],
            [' ', ' ', ' ', ' ']
        ]

        print(matrix_to_text(expected))
        print(matrix_to_text(source))
