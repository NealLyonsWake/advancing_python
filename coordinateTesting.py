"""
Assertion Exercise:
Assume a cartesian cordinate space R = R(x,y,z).
Each of the co-ordinates, (x,y,z) can have only integer values >= 0 The maximum value each of the co-odinates can assume,
and the sum of all three co-ordinates (the tuple) is capped at integer N.
Using assertion, verify that a given set of coordintes match the expectation for a set value of N = 7.

coordinates:
R1 = (1, 4, 2)
R2 = (3, 1, 9)
R3 = (0, 3, 4)
R4 = (1, 2, 0)
R5 = (-3, 12 , -5)
"""

from coordinates import spaceR
import unittest

R1 = (1, 4, 2)
R2 = (3, 1, 9)
R3 = (0, 3, 4)
R4 = (1, 2, 0)
R5 = (-3, 12, -5)


class TestCoordinates(unittest.TestCase):
    def test_R_are_above_zero(self):
        """
        Test will fail if no R tuple value is < 0; tests error handler only. 
        """
        self.assertRaises(ValueError, spaceR, -3, 12, -5)

    def test_R_conforms_to_N(self):
        """
        Tests R tuple fully conforms to >= 0 and no individual or summed R tuple coordinate exceeds N = 7. 
        """
        self.assertTrue(spaceR(1, 2, 0))


if __name__ == "__main__":
    unittest.main()
