import unittest


def min_pos():
    return ord('A')


def build_array():
    array = []
    max_pos = ord('z')
    for i in range(min_pos(), max_pos):
        array.append(0)
    return array


def get_pos(char):
    char_pos = ord(char)
    return char_pos - min_pos()


def compress(string):
    array = build_array()

    min_pos_read = len(array)
    max_pos_read = 0

    for char in string:
        pos = get_pos(char)
        array[pos] += 1
        if min_pos_read > pos:
            min_pos_read = pos
        if max_pos_read < pos:
            max_pos_read = pos

    result = ""

    min_pos_value = min_pos()

    for i in range(min_pos_read, max_pos_read + 1):
        if array[i] > 0:
            char = chr(i + min_pos_value)
            result += char + str(array[i])

    if len(result) < len(string):
        return result
    else:
        return string


class TestFunctions(unittest.TestCase):
    def testLong(self):
        self.assertEqual("a2b1c5d4e3", compress("aabcccccddddeee"))

    def testShort(self):
        self.assertEqual("abc", compress("abc"))
