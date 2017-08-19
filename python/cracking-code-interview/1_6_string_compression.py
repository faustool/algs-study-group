import unittest


# return the minimal integer representation of a the A character (65)
def get_min_char_int_value():
    return ord('A')


# build an array with enough size to fit chars ranging from A to z
def build_array():
    array = []
    max_char_int_value = ord('z')
    for i in range(get_min_char_int_value(), max_char_int_value):
        array.append(0)
    return array


# get the possible position of a char in the array. e.g. A (char 65) will be in position 0
def calculate_pos(char):
    char_int_value = ord(char)
    return char_int_value - get_min_char_int_value()


# compress the given string
def compress(string):
    array = build_array()

    min_pos = len(array)
    max_pos = 0

    for char in string:
        pos = calculate_pos(char)
        array[pos] += 1
        if min_pos > pos:
            min_pos = pos
        if max_pos < pos:
            max_pos = pos

    result = ""

    min_char_int_value = get_min_char_int_value()

    for i in range(min_pos, max_pos + 1):
        if array[i] > 0:
            char = chr(i + min_char_int_value)
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
