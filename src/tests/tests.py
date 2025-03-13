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

    def test_addition_6(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.addition(0, 0.1)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, 0.1)

    def test_addition_7(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.addition(4.75, 2.25)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, 7)

    def test_addition_8(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.addition(10.18, 0.57)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, 10.75)

    def test_addition_9(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.addition(-5.4, 1.2)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, -4.4)

    def test_addition_10(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.addition(-128.77, -41.22)     #the name of the function has to corespond with name here "addition"
        self.assertEqual(result, -169.99)
#############################################################################################################################
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

    def test_subtraction_6(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(4.2, 0.2)     #the name of the function has to corespond with name here "subtraction"
        self.assertEqual(result, 4)

    def test_subtraction_7(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(15, 4.75)     #the name of the function has to corespond with name here "subtraction"
        self.assertEqual(result, 10.25)

    def test_subtraction_8(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(-5.4, 2.6)     #the name of the function has to corespond with name here "subtraction"
        self.assertEqual(result, -8)

    def test_subtraction_9(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(-8.5, -3.3)     #the name of the function has to corespond with name here "subtraction"
        self.assertEqual(result, -5.2)

    def test_subtraction_10(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(1500, 0.01)     #the name of the function has to corespond with name here "subtraction"
        self.assertEqual(result, 1499.99)
#############################################################################################################################
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

    def test_multiplication_6(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(10, 1.5)     #the name of the function has to corespond with name here "multiplication"
        self.assertEqual(result, 15)

    def test_multiplication_7(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(5.4, 2.7)     #the name of the function has to corespond with name here "multiplication"
        self.assertEqual(result, 14.58)

    def test_multiplication_8(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(10, 0.7)     #the name of the function has to corespond with name here "multiplication"
        self.assertEqual(result, 7)

    def test_multiplication_9(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(-100, 2.5)     #the name of the function has to corespond with name here "multiplication"
        self.assertEqual(result, -250)

    def test_multiplication_10(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(-12.48, -0)     #the name of the function has to corespond with name here "multiplication"
        self.assertEqual(result, 0)
#############################################################################################################################
    def test_division_1(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(10, 10)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, 1)

    def test_division_2(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(5, 1)     #the name of the function has to corespond with name here "division", 5 = dividend, 1 = divisor
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

    def test_division_6(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(10.5, 2)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, 5.25)

    def test_division_7(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(22, 2.2)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, 10)

    def test_division_8(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(10, 8)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, 1.25)

    def test_division_9(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(16.5, 2.5)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, 6.6)

    def test_division_10(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(-10500, -2.795)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, 3756.70841)

    def test_division_error_1(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(8, 0)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, "error")       #add error name

    def test_division_error_2(self):
        module_name = "math_lib"                 #the name of the math library has to corespond with name here "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.division(8, -0)     #the name of the function has to corespond with name here "division"
        self.assertEqual(result, "error")       #add error name
#############################################################################################################################    
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
#############################################################################################################################
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

    def test_expon_8(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(2.2, 2)        #the first argument is number, second is exponent: 15^10
        self.assertEqual(result, 4.84)

    def test_expon_9(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(14.65, 3)        #the first argument is number, second is exponent: 15^10
        self.assertEqual(result, 3144.219625)
#############################################################################################################################
    def test_root_1(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(4, 2)        #the name of the function has to corespond with name here "root", the first argument is number, second is root
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

    def test_root_6(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(2.5, 2)        #the first argument is number, second is root
        self.assertEqual(result, 1.58114)

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
#############################################################################################################################
    def test_ln_1(self):
        module_name = "math_lab"
        math_module = importlib.import_module(module_name)
        result = math_module.ln(1)              #the name of the function has to corespond with name here "ln"
        self.assertEqual(result, 0)

    def test_ln_2(self):
        module_name = "math_lab"
        math_module = importlib.import_module(module_name)
        result = math_module.ln(2)              #the name of the function has to corespond with name here "ln"
        self.assertEqual(result, 0.693147)

    def test_ln_3(self):
        module_name = "math_lab"
        math_module = importlib.import_module(module_name)
        result = math_module.ln(150)              #the name of the function has to corespond with name here "ln"
        self.assertEqual(result, 5.01064)

    def test_ln_4(self):
        module_name = "math_lab"
        math_module = importlib.import_module(module_name)
        result = math_module.ln(150000)              #the name of the function has to corespond with name here "ln"
        self.assertEqual(result, 11.91839)

    def test_ln_5(self):
        module_name = "math_lab"
        math_module = importlib.import_module(module_name)
        result = math_module.ln(8.4)              #the name of the function has to corespond with name here "ln"
        self.assertEqual(result, 2.12823)

    def test_ln_error_1(self):
        module_name = "math_lab"
        math_module = importlib.import_module(module_name)
        result = math_module.ln(0)              #the name of the function has to corespond with name here "ln"
        self.assertEqual(result, "error")

    def test_ln_error_2(self):
        module_name = "math_lab"
        math_module = importlib.import_module(module_name)
        result = math_module.ln(-1)              #the name of the function has to corespond with name here "ln"
        self.assertEqual(result, "error")


if __name__ == '__main__':
    unittest.main()
    
# end of tests.py