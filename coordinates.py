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
R5 = (-3, 12, -5)
"""


def spaceR(x, y, z):
    n = 7
    sum_r = x + y + z
    if x < 0 or y < 0 or z < 0:
        raise ValueError("R coordinates should be >= 0")
    elif x <= n and y <= n and z <= n:
        if sum_r > n:
            return sum_r
        else:
            return True
    else:
        return False

#print(spaceR(-3, 12, -5))       