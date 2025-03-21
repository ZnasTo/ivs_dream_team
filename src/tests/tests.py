##  
# @author xkubisa00, Aleš Kubiš
# 
#   This file contains tests for math library

import unittest
import importlib


class TestMathLib(unittest.TestCase):
    def test_addition_1(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.addition(1, 1)     
        self.assertEqual(result, 2)
    
    def test_addition_2(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.addition(5, 10)     
        self.assertEqual(result, 15)
    
    def test_addition_3(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.addition(152000, 48000)     
        self.assertEqual(result, 200000)
    
    def test_addition_4(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.addition(-1, -1)     
        self.assertEqual(result, -2)
    
    def test_addition_5(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.addition(5, -10)     
        self.assertEqual(result, -5)

    def test_addition_6(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.addition(0, 0.1)     
        self.assertEqual(result, 0.1)

    def test_addition_7(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.addition(4.75, 2.25)     
        self.assertEqual(result, 7)

    def test_addition_8(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.addition(10.18, 0.57)     
        self.assertEqual(result, 10.75)

    def test_addition_9(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.addition(-5.4, 1.2)     
        self.assertEqual(result, -4.2)

    def test_addition_10(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.addition(-128.77, -41.22)     
        self.assertEqual(result, -169.99)
#############################################################################################################################
    def test_subtraction_1(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(2, 1)     
        self.assertEqual(result, 1)

    def test_subtraction_2(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(15, 4)     
        self.assertEqual(result, 11)

    def test_subtraction_3(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(182000, 32000)     
        self.assertEqual(result, 150000)

    def test_subtraction_4(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(-2, 3)     
        self.assertEqual(result, -5)

    def test_subtraction_5(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(-5, -15)     
        self.assertEqual(result, 10)

    def test_subtraction_6(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(4.2, 0.2)     
        self.assertEqual(result, 4)

    def test_subtraction_7(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(15, 4.75)     
        self.assertEqual(result, 10.25)

    def test_subtraction_8(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(-5.4, 2.6)     
        self.assertEqual(result, -8)

    def test_subtraction_9(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(-8.5, -3.3)     
        self.assertEqual(result, -5.2)

    def test_subtraction_10(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.subtraction(1500, 0.01)     
        self.assertEqual(result, 1499.99)
#############################################################################################################################
    def test_multiplication_1(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(2, 3)     
        self.assertEqual(result, 6)

    def test_multiplication_2(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(10, 1)     
        self.assertEqual(result, 10)
    
    def test_multiplication_3(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(526, 0)     
        self.assertEqual(result, 0)

    def test_multiplication_4(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(15, -2)     
        self.assertEqual(result, -30)

    def test_multiplication_5(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(-10, -20)     
        self.assertEqual(result, 200)

    def test_multiplication_6(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(10, 1.5)     
        self.assertEqual(result, 15)

    def test_multiplication_7(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(5.4, 2.7)     
        self.assertEqual(result, 14.58)

    def test_multiplication_8(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(10, 0.7)     
        self.assertEqual(result, 7)

    def test_multiplication_9(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(-100, 2.5)     
        self.assertEqual(result, -250)

    def test_multiplication_10(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.multiplication(-12.48, -0)     
        self.assertEqual(result, 0)
#############################################################################################################################
    def test_division_1(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(10, 10)     
        self.assertEqual(result, 1)

    def test_division_2(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(5, 1)     #5 = dividend, 1 = divisor
        self.assertEqual(result, 5)

    def test_division_3(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(21, 7)     
        self.assertEqual(result, 3)

    def test_division_4(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(-10, 2)     
        self.assertEqual(result, -5)

    def test_division_5(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(-25, -5)     
        self.assertEqual(result, 5)

    def test_division_6(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(10.5, 2)     
        self.assertEqual(result, 5.25)

    def test_division_7(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(22, 2.2)     
        self.assertEqual(result, 10)

    def test_division_8(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(10, 8)     
        self.assertEqual(result, 1.25)

    def test_division_9(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(16.5, 2.5)     
        self.assertEqual(result, 6.6)

    def test_division_10(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(-10500, -2.795)     
        self.assertEqual(result, 3756.70841)

    def test_division_error_1(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(8, 0)     
        self.assertEqual(result, "Error!")       

    def test_division_error_2(self):
        module_name = "math_lib"                 
        math_module = importlib.import_module(module_name)
        result = math_module.division(8, -0)     
        self.assertEqual(result, "Error!")       
#############################################################################################################################    
    def test_factorial_1(self):
        module_name = "math_lib"                
        math_module = importlib.import_module(module_name)
        result = math_module.factorial(5)       
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
        self.assertEqual(result, "Error!")           
#############################################################################################################################
    def test_expon_1(self):
        module_name = "math_lib"                
        math_module = importlib.import_module(module_name)
        result = math_module.expon(2, 2)        #the first argument is number, second is exponent: 2^2
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
        result = math_module.expon(2.2, 2)        #the first argument is number, second is exponent: 2.2^2
        self.assertEqual(result, 4.84)

    def test_expon_9(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(14.65, 3)        #the first argument is number, second is exponent: 14.65^3
        self.assertEqual(result, 3144.219625)

    def test_expon_error_1(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(10, 1.5)        #the first argument is number, second is exponent: 10^1.5
        self.assertEqual(result, "Error!")

    def test_expon_error_2(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.expon(10, -2)        #the first argument is number, second is exponent: 10^-2
        self.assertEqual(result, "Error!")
#############################################################################################################################
    def test_root_1(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(4, 2)        #the name of the function has to corespond with name here "root", the first argument is number, second is root
        self.assertEqual(result, 2)

    def test_root_2(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(64, 2)        #the first argument is number, second is root
        self.assertEqual(result, 8)

    def test_root_3(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(8, 3)        #the first argument is number, second is root
        self.assertEqual(result, 2)

    def test_root_4(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(-8, 3)        #the first argument is number, second is root
        self.assertEqual(result, -2)

    def test_root_5(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(8000000, 3)        #the first argument is number, second is root
        self.assertEqual(result, 200)

    def test_root_6(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(2.5, 2)        #the first argument is number, second is root
        self.assertEqual(result, 1.58114)

    def test_root_error_1(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(8, 0)        #the first argument is number, second is root
        self.assertEqual(result, "Error!")        

    def test_root_error_2(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(8, 1)        #the first argument is number, second is root
        self.assertEqual(result, "Error!")        

    def test_root_error_3(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(-8, 1)        #the first argument is number, second is root
        self.assertEqual(result, "Error!")        

    def test_root_error_4(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(-8, 0)        #the first argument is number, second is root
        self.assertEqual(result, "Error!")        

    def test_root_error_5(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(-8, -3)        #the first argument is number, second is root
        self.assertEqual(result, "Error!")        

    def test_root_error_6(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.root(8, -3)        #the first argument is number, second is root
        self.assertEqual(result, "Error!")        
#############################################################################################################################
    def test_abs_1(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.abs(1)
        self.assertEqual(result, 1)

    def test_abs_2(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.abs(0)
        self.assertEqual(result, 0)

    def test_abs_3(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.abs(-1)
        self.assertEqual(result, 1)

    def test_abs_4(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.abs(13.58)
        self.assertEqual(result, 13.58)

    def test_abs_5(self):
        module_name = "math_lib"
        math_module = importlib.import_module(module_name)
        result = math_module.abs(-13.58)
        self.assertEqual(result, 13.58)


if __name__ == '__main__':
    unittest.main()
    
# end of tests.py