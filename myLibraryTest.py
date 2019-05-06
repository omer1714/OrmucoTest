import unittest
from myLibrary import compare

class myLibraryTest(unittest.TestCase):

    def test1_Greater(self):
        strCompare = compare('1.1.2', '1.0')
        self.assertEqual(strCompare, 1)

    def test2_Greater(self):
        strCompare = compare('5.1.2', '2.3.7')
        self.assertEqual(strCompare, 1)

    def test3_Greater(self):
        strCompare = compare('8', '7.1.1')
        self.assertEqual(strCompare, 1)

    def test1_Equal(self):
        strCompare = compare('1.1', '1.1.0')
        self.assertEqual(strCompare, 0)

    def test2_Equal(self):
        strCompare = compare('2.8', '2.8')
        self.assertEqual(strCompare, 0)

    def test3_Equal(self):
        strCompare = compare('1.0.0', '1')
        self.assertEqual(strCompare, 0)

    def test1_Less(self):
        strCompare = compare('6.3', '7.1.1')
        self.assertEqual(strCompare, -1)

    def test2_Less(self):
        strCompare = compare('0.0', '0.1')
        self.assertEqual(strCompare, -1)

    def test3_Less(self):
        strCompare = compare('7.9.11', '9.0.1')
        self.assertEqual(strCompare, -1)


unittest.main()