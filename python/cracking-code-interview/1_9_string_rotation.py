import unittest

def isRotation(s1, s2):
    return isSubstring(s1, s2 + s2)

def isSubstring(s1, s2):
    return s1 in s2

class TestFunctions(unittest.TestCase):
    def testIsRotation(self):
        self.assertTrue(isRotation("waterbottle", "erbottlewat"))
        self.assertTrue(isRotation("waterbottle", "bottlewater"))
        self.assertTrue(isRotation("waterbottle", "ttlewaterbo"))
        self.assertTrue(isRotation("waterbottle", "terbottlewa"))
        self.assertTrue(isRotation("waterbottle", "waterbottle"))
        self.assertTrue(isRotation("waterbottle", "aterbottlew"))
        self.assertTrue(isRotation("waterbottle", "lewaterbott"))
        self.assertFalse(isRotation("waterbottle", "watexbottle"))

