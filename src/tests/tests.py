##  @author xkubisa00, Aleš Kubiš
# 
#   This file contains tests for math library

import unittest
import importlib


## @todo add more tests that test doubles,...
# @todo add error names
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

    def test_multiplication_1(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(2, 3)     #the name of the function has to corespond with name here "multiplication"
        self.assertEqual(result, 6)

    def test_multiplication_2(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(10, 1)     #the name of the function has to corespond with name here "multiplication"
        self.assertEqual(result, 10)
    
    def test_multiplication_3(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(526, 0)     #the name of the function has to corespond with name here "multiplication"
        self.assertEqual(result, 0)

    def test_multiplication_4(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(15, -2)     #the name of the function has to corespond with name here "multiplication"
        self.assertEqual(result, -30)

    def test_multiplication_5(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(-10, -20)     #the name of the function has to corespond with name here "multiplication"
        self.assertEqual(result, 200)

    def test_division_1(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(10, 10)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, 1)

    def test_division_2(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(5, 1)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, 5)

    def test_division_3(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(21, 7)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, 3)

    def test_division_4(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(-10, 2)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, -5)

    def test_division_5(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(-25, -5)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, 5)

    def test_division_error(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(8, 0)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, "error")       #add error name
    
    def test_factorial_1(self):
        module_name = "math_lib"                #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.factorial(5)       #the name of the function has to corespond with name here "factorial"
        self.assertEqual(120)

    def test_factorial_2(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.factorial(0)
        self.assertEqual(0)

    def test_factorial_3(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.factorial(12)
        self.assertEqual(result, 479001600)

    def test_factorial_4(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.factorial(100)
        self.assertEqual(result,  0)        #result should be  9.332621544 E+157, need to discuss how are we going to display this

    def test_factorial_error(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.factorial(-1)
        self.assertEqual(result, "error")           #add error name

    def test_expon_1(self):
        module_name = "math_lib"                #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(2, 2)        #the name of the function has to corespond with name here "expon", the first argument is number, second is exponent: 2^2
        self.assertEqual(result, 4)

    def test_expon_2(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(2, 3)        #the first argument is number, second is exponent: 2^3
        self.assertEqual(result, 8)

    def test_expon_3(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(10, 0)        #the first argument is number, second is exponent: 10^0
        self.assertEqual(result, 1)

    def test_expon_4(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(-5, 2)        #the first argument is number, second is exponent: -5^2
        self.assertEqual(result, 25)

    def test_expon_5(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(-2, 5)        #the first argument is number, second is exponent: -2^5
        self.assertEqual(result, -32)

    def test_expon_6(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(15, 10)        #the first argument is number, second is exponent: 15^10
        self.assertEqual(result, 576650390625)

    def test_expon_7(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(111, 15)        #the first argument is number, second is exponent: 111^15
        self.assertEqual(result, 0)                 #result should be  4.7845894883377 E+30, need to discuss how are we going to display this

    def test_root_1(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(4, 2)        #the first argument is number, second is root
        self.assertEqual(result, 2)

    def test_root_2(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(64, 2)        #the first argument is number, second is root
        self.assertEqual(result, 8)

    def test_root_3(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(8, 3)        #the first argument is number, second is root
        self.assertEqual(result, 2)

    def test_root_4(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(-8, 3)        #the first argument is number, second is root
        self.assertEqual(result, -2)

    def test_root_5(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(8000000, 3)        #the first argument is number, second is root
        self.assertEqual(result, 200)

    def test_root_error_1(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(8, 0)        #the first argument is number, second is root
        self.assertEqual(result, "error")        #add error name

    def test_root_error_2(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(8, 1)        #the first argument is number, second is root
        self.assertEqual(result, "error")        #add error name

    def test_root_error_3(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(-8, 1)        #the first argument is number, second is root
        self.assertEqual(result, "error")        #add error name

    def test_root_error_4(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(-8, 0)        #the first argument is number, second is root
        self.assertEqual(result, "error")        #add error name

    def test_root_error_5(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(-8, -3)        #the first argument is number, second is root
        self.assertEqual(result, "error")        #add error name

    def test_root_error_6(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(8, -3)        #the first argument is number, second is root
        self.assertEqual(result, "error")        #add error name

#add ln funkcion tests


if __name__ == '__main__':
    unittest.main()
    
# end of tests.py