import sys 
from pathlib import Path
import unittest

sys.path.append(str(Path(__file__).parent.parent))
    
from src.directory import Student

class TestStudent(unittest.TestCase):
    def setUp(self):  
        """Set up test fixture for each method"""
        self.student = Student("Aman", 15,10)
    
    def test_student_initialization(self):
        """Test student initialization"""
        self.assertEqual(self.student.name, "Aman")
        self.assertEqual(self.student.age, 15)
        self.assertEqual(self.student.grade, 10)
        self.assertEqual(self.student.get_courses(), {})
        
    def test_add_course(self):
        """Test adding a course"""
        self.student.add_course({'math': 50})
        self.assertEqual(self.student.get_courses(), {'math': 50})
        
        self.student.add_course({'science': 78})
        self.assertEqual(self.student.get_courses(), {'math': 50, 'science': 78})
    
    def test_get_courses(self):     
        """Test getting courses"""
        self.student.add_course({'math': 50})
        self.student.add_course({'science': 78})
        self.assertEqual(self.student.get_courses(), {'math': 50, 'science': 78})
    

if __name__ == '__main__':
    unittest.main()
