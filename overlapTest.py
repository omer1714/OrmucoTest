import unittest
from overlap import isOverlapping

class overlapTest(unittest.TestCase):

    def test_zeroOverlap(self):
        result = isOverlapping(0, 0, 0, 0)
        self.assertEqual(result, True)

    def test_positiveOverlap(self):
        result = isOverlapping(2, 5, 3, 6)
        self.assertEqual(result, True)

    def test_positiveNoOverLap(self):
        result = isOverlapping(0, 4, 6, 9)
        self.assertEqual(result, False)

    def test_negativeOverLap(self):
        result = isOverlapping(-7, -3, -5, -1)
        self.assertEqual(result, True)

    def test_negativeNoOverLap(self):
        result = isOverlapping(-5, -1, -8, -6)
        self.assertEqual(result, True)

    def test_mixOverLap(self):
        result = isOverlapping(-1, 2, 0, -2)
        self.assertEqual(result, True)

    def test_mixNoOverLaps(self):
        result = isOverlapping(-5, -4, 3, 8)
        self.assertEqual(result, False)

unittest.main()