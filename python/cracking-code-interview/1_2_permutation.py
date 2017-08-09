import unittest


def permutation_o_n_log_n(s1, s2):
    if len(s1) != len(s2):
        return False

    search_indexes = list(range(len(s1)))
    for c in s2:
        found = False
        for i in range(len(search_indexes)):
            if s1[search_indexes[i]] == c:
                del search_indexes[i]
                found = True
                break
        if not found:
            return False
    return True


def permutation_o_n(s1, s2):
    if len(s1) != len(s2):
        return False

    hash_table = []
    for i in range(20):
        hash_table.append([])

    for c in s1:
        hash_code = ord(c) % len(hash_table)
        hash_list = hash_table[hash_code]
        hash_list.append(c)

    for c in s2:
        hash_code = ord(c) % len(hash_table)
        hash_list = hash_table[hash_code]
        found = False
        for i in range(len(hash_list)):
            if c == hash_list[i]:
                del hash_list[i]
                found = True
                break
        if not found:
            return False

    return True


class TestFunctions(unittest.TestCase):
    def test_o_n_log_n(self):
        self.assertTrue(permutation_o_n_log_n("asd", "asd"))
        self.assertTrue(permutation_o_n_log_n("asd", "ads"))
        self.assertTrue(permutation_o_n_log_n("asd", "das"))
        self.assertTrue(permutation_o_n_log_n("asd", "sad"))
        self.assertTrue(permutation_o_n_log_n("asd", "sda"))
        self.assertTrue(permutation_o_n_log_n("asd", "dsa"))
        self.assertFalse(permutation_o_n_log_n("asd", "qwe"))
        self.assertFalse(permutation_o_n_log_n("asd", "aad"))
        self.assertFalse(permutation_o_n_log_n("asd", "aaa"))
        self.assertFalse(permutation_o_n_log_n("asd", "aaaa"))

    def test_o_n(self):
        self.assertTrue(permutation_o_n("asd", "asd"))
        self.assertTrue(permutation_o_n("asd", "ads"))
        self.assertTrue(permutation_o_n("asd", "das"))
        self.assertTrue(permutation_o_n("asd", "sad"))
        self.assertTrue(permutation_o_n("asd", "sda"))
        self.assertTrue(permutation_o_n("asd", "dsa"))
        self.assertFalse(permutation_o_n("asd", "qwe"))
        self.assertFalse(permutation_o_n("asd", "aad"))
        self.assertFalse(permutation_o_n("asd", "aaa"))
        self.assertFalse(permutation_o_n("asd", "aaaa"))
