import unittest
import importlib

class TestMathLib(unittest.TestCase):
    def test_addition_1(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.addition(1, 1)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, 2)
    
    def test_addition_2(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.addition(5, 10)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, 15)
    
    def test_addition_3(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.addition(152000, 48000)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, 160000)
    
    def test_addition_4(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.addition(-1, -1)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, -2)
    
    def test_addition_5(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.addition(5, -10)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, -5)
    
    def test_subtraction_1(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(2, 1)     #the name of the function has to corespond with name here "subtraction"
        self.assertEqual(result, 1)

    def test_subtraction_2(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(15, 4)     #the name of the function has to corespond with name here "subtraction"
        self.assertEqual(result, 11)

    def test_subtraction_3(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(182000, 32000)     #the name of the function has to corespond with name here "subtraction"
        self.assertEqual(result, 150000)

    def test_subtraction_4(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(-2, 3)     #the name of the function has to corespond with name here "subtraction"
        self.assertEqual(result, -5)

    def test_subtraction_5(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(-5, -15)     #the name of the function has to corespond with name here "subtraction"
        self.assertEqual(result, 10)
    



if __name__ == '__main__':
    unittest.main()
    
