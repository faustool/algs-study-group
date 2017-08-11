import unittest


def urlify_n_square(given_string):
    string = list(given_string)
    full_length = len(string)
    i = 0
    while i < full_length:
        if string[i] == ' ':
            for j in range(full_length - 1, i + 2, -1):
                string[j] = string[j - 2]
            string[i] = '%'
            string[i + 1] = '2'
            string[i + 2] = '0'
            i += 3
        else:
            i += 1
    return ''.join(string)


def urlify_n(given_string, length):
    string = list(given_string)
    full_length = len(string)
    i = full_length - 1
    j = length - 1
    while j > 0:
        if string[j] == ' ':
            string[i] = '0'
            string[i - 1] = '2'
            string[i - 2] = '%'
            i -= 3
        else:
            string[i] = string[j]
            i -= 1
        j -= 1
    return ''.join(string)


class TestFunctions(unittest.TestCase):
    def test_book_example(self):
        self.assertEqual(urlify_n_square('Mr John Smith    '), 'Mr%20John%20Smith')
        self.assertEqual(urlify_n('Mr John Smith    ', 13), 'Mr%20John%20Smith')

    def test_long_shot(self):
        self.assertEqual(urlify_n_square('My        N                '), 'My%20%20%20%20%20%20%20%20N')
        self.assertEqual(urlify_n('My        N                ', 11), 'My%20%20%20%20%20%20%20%20N')
