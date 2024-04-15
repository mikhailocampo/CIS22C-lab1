import unittest
from lab1 import isArrayPrimeIter

class TestPrimeArrayChecker(unittest.TestCase):
    def test_empty_array(self):
        self.assertTrue(isArrayPrimeIter([], 0), "An empty array should be considered as having all primes.")

    def test_all_primes(self):
        self.assertTrue(isArrayPrimeIter([2, 3, 5, 7, 11], 5), "Array with all primes should return True.")

    def test_no_primes(self):
        self.assertFalse(isArrayPrimeIter([1, 4, 6, 8, 10], 5), "Array with no primes should return False.")

    def test_mixed_numbers(self):
        self.assertFalse(isArrayPrimeIter([2, 3, 4, 5, 6], 5), "Array with both primes and non-primes should return False.")

    def test_with_zero_and_one(self):
        self.assertFalse(isArrayPrimeIter([0, 1, 5, 7], 4), "Array containing 0 and 1 should return False.")

    def test_negative_numbers(self):
        self.assertFalse(isArrayPrimeIter([-2, -3, -5, -7], 4), "Array with negative numbers should return False.")
    
    def test_large_numbers(self):
        self.assertTrue(isArrayPrimeIter([1000000007, 1000000009, 1000000021], 3), "Array with large primes should return True.")

if __name__ == '__main__':
    unittest.main()