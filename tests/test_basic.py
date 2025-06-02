import sys 
from pathlib import Path
import unittest

sys.path.append(str(Path(__file__).parent.parent))
    
from src.basic import add, subtract, multiply, divide


class TestBasicOperations(unittest.TestCase): 
    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    def test_subtract(self):  
        """Test the subtract function."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, -1), 0)
    def test_multiply(self):
        """Test the multiply function."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)
    def test_divide(self):
        """Test the divide function."""
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertRaises(ValueError, divide, 5, 0)
    def test_divide_by_zero(self):
        """Test dividing by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)
if __name__ == '__main__':
    unittest.main()


