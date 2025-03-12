import unittest
import importlib

class Test_math_lib(unittest.TestCase):
    def test_addition_1(self):
        modul_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(modul_name)
        result = math_module.addition(1, 1)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, 2)
    
    def test_addition_2(self):
        modul_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(modul_name)
        result = math_module.addition(5, 10)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, 15)
    
    def test_addition_3(self):
        modul_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(modul_name)
        result = math_module.addition(152000, 48000)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, 160000)
    
    def test_addition_4(self):
        modul_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(modul_name)
        result = math_module.addition(-1, -1)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, -2)
    
    def test_addition_5(self):
        modul_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(modul_name)
        result = math_module.addition(5, -10)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, -5)



if __name__ == '__main__':
    unittest.main()
    
