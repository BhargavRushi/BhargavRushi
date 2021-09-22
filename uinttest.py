import unittest

def prime(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True

class TestPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(prime(11),True)

    def test_02(self):
        self.assertEqual(prime(12),False)

    def test_03(self):
        self.assertEqual(prime(13),True)

    def test_03(self):
        self.assertEqual(prime(27),False)

if "__name__" == "__main()__":
    unittest.main(verbosity = 2)

