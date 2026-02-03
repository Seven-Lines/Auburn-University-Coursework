import unittest
import source  # type: ignore


class TestCalc(unittest.TestCase):

    # -----------------
    # performMultiply
    # -----------------
    def testMultiplySuccess1(self):
        self.assertEqual(6, source.performMultiply(2, 3))

    def testMultiplySuccess2(self):
        self.assertEqual(-10, source.performMultiply(-2, 5))

    def testMultiplyFail1(self):
        self.assertNotEqual(7, source.performMultiply(2, 3))

    def testMultiplyFail2(self):
        self.assertNotEqual(0, source.performMultiply(4, 5))


    # -----------------
    # performDivision
    # -----------------
    def testDivisionSuccess1(self):
        self.assertEqual(5, source.performDivision(10, 2))

    def testDivisionSuccess2(self):
        self.assertAlmostEqual(2.5, source.performDivision(5, 2))

    def testDivisionFail1(self):
        with self.assertRaises(ValueError):
            source.performDivision(10, 0)

    def testDivisionFail2(self):
        with self.assertRaises(ValueError):
            source.performDivision(-3, 0)


    # -----------------
    # performSquareRoot
    # -----------------
    def testSquareRootSuccess1(self):
        self.assertEqual(4, source.performSquareRoot(16))

    def testSquareRootSuccess2(self):
        self.assertEqual(5, source.performSquareRoot(25))

    def testSquareRootFail1(self):
        with self.assertRaises(ValueError):
            source.performSquareRoot(-1)

    def testSquareRootFail2(self):
        with self.assertRaises(ValueError):
            source.performSquareRoot(-100)


if __name__ == '__main__':
    unittest.main()
