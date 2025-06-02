import sys 
from pathlib import Path
import unittest

sys.path.append(str(Path(__file__).parent.parent))


class TestAssertionMethods(unittest.TestCase):  
    def test_equality(self): 
        self.assertEqual(1 + 1, 2)  
        self.assertNotEqual(1 + 1, 3)  
    def test_boolean(self):  
        self.assertTrue(1 <2)
        self.assertFalse(1>2)
        self.assertTrue(False) # should fail
        self.assertFalse(True) #Should fail
    def test_is_none(self): 
        self.assertIsNone(None) 
        self.assertIsNotNone(1)
    def test_is_instance(self):  
        self.assertIsInstance('hello', str)
        self.assertNotIsInstance(123, str)
        self.assertIsInstance(123,int)
        self.assertIsInstance(123, float) #should fail 
        self.assertIsInstance({'a':[1,2,3]}, dict)
        self.assertIsInstance([1,2,3], list)
        self.assertIsInstance((1,2,3), tuple) # this should pass! 
        self.assertIsInstance({1,2,3}, set)
    def test_inheritance(self):  
        class Animal: pass 
        class Dog(Animal): pass
        
        my_dog = Dog() 
        self.assertIsInstance(my_dog, Dog)
        self.assertIsInstance(my_dog, Animal) 
        
    def test_abstract_class(self):
        from abc import ABC, abstractmethod
        
        class AbstractClass(ABC):
            @abstractmethod
            def my_method(self):
                pass
        
        class ConcreteClass(AbstractClass):
            def my_method(self):
                return "Implemented"
            
        concerte_class_instance  = ConcreteClass()
        print(type(concerte_class_instance))
        self.assertIsInstance(concerte_class_instance , AbstractClass)
        self.assertIsInstance(concerte_class_instance , ConcreteClass)
        
    def test_member(self): 
        ls = [1,2,3]
        self.assertIn(2, ls)
        self.assertNotIn(4, ls)
    def test_raises(self): 
        with self.assertRaises(ValueError):
            raise ValueError("This is a ValueError")
        
        with self.assertRaises(TypeError):
            raise TypeError("This is a TypeError")
        with self.assertRaises(NameError):
            raise NameError("This is a NameError")
        
        with self.assertRaises(SyntaxError):
            eval('x === 1')

        with self.assertRaises(ZeroDivisionError):
            1 / 0
        with self.assertRaises(AssertionError):
            self.assertEqual(1, 2, "This should raise an AssertionError")
            
        with self.assertRaises(Exception):
            raise Exception("This is a general exception")
        
        with self.assertRaises(ArithmeticError):    
            1 / 0
            
        with self.assertRaises(KeyError):
            d = {}
            value = d['key']  
                    
        with self.assertRaises(IndexError): 
            lst = [1, 2, 3]
            value = lst[5]
            
        with self.assertRaises(AttributeError):
            class MyClass:
                """class with no methods"""
                pass
            obj = MyClass()
            obj.non_existent_method()  
        with self.assertRaises(IOError):
            with open('non_existent_file.txt', 'r') as f:
                content = f.read()
        with self.assertRaises(OSError):
            import os
            os.remove('non_existent_file.txt')
        with self.assertRaises(NotImplementedError):                                
            class MyClass:
                def my_method(self):
                    raise NotImplementedError("This method is not implemented")
            obj = MyClass()
            obj.my_method()
        with self.assertRaises(ImportError):
            import non_existent_module
            
        with self.assertRaises(ValueError):
            int("not a number")
            
        with self.assertRaises(TypeError):
            "string" + 1      
                  
        with self.assertRaises(TimeoutError):
            import time
            time.sleep(5)
            raise TimeoutError("Operation timed out")
        with self.assertRaises(OverflowError):          
            import math
            math.exp(1000)

        with self.assertRaises(RecursionError):
            def recursive_function():
                return recursive_function()
            recursive_function()
        with self.assertRaises(AssertionError):
            self.assertTrue(False, "This assertion should fail")
        with self.assertRaises(ImportError):
            import non_existent_module

        

if __name__ == '__main__':
    unittest.main()

        