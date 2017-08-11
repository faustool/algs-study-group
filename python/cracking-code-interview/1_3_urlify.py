import unittest


def urlify_n_square(string, length):
    changeable = list(string)
    full_length = len(changeable)
    i = 0
    while i < full_length:
        if changeable[i] == ' ':
            for j in range(full_length - 1, i + 2, -1):
                changeable[j] = changeable[j - 2]
            changeable[i] = '%'
            changeable[i + 1] = '2'
            changeable[i + 2] = '0'
            i += 3
        else:
            i += 1
    return ''.join(changeable)


class TestFunctions(unittest.TestCase):
    def test_book_example(self):
        self.assertEqual(urlify_n_square('Mr John Smith    ', 13), 'Mr%20John%20Smith')
