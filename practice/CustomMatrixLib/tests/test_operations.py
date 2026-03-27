import unittest
import numpy as np
import sys
import os

# Adds the src directory to the path so we can import our library
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.matrix_operations import CustomMatrixLib

class TestMatrixOperations(unittest.TestCase):
    
    def setUp(self):
        self.lib = CustomMatrixLib()
        self.mat_a = np.array([[1, 2], [3, 4], [5, 6]]) # 3x2
        self.mat_b = np.array([[7, 8], [9, 10]])        # 2x2

    def test_transpose(self):
        """Verify manual transpose matches NumPy's .T method"""
        custom_res = self.lib.transpose(self.mat_a)
        numpy_res = self.mat_a.T
        np.testing.assert_array_equal(custom_res, numpy_res)

    def test_multiplication(self):
        """Verify manual multiplication matches NumPy's @ operator"""
        custom_res = self.lib.multiply(self.mat_a, self.mat_b)
        numpy_res = self.mat_a @ self.mat_b
        np.testing.assert_array_equal(custom_res, numpy_res)

    def test_invalid_multiplication(self):
        """Ensure the library raises an error for incompatible shapes"""
        with self.assertRaises(ValueError):
            # Trying to multiply 3x2 by 3x2 (should fail)
            self.lib.multiply(self.mat_a, self.mat_a)

if __name__ == "__main__":
    unittest.main()