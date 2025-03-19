## @author xturcam00 Martin Turčan
#
# File contains math library for calculator 


##
# @brief Function adds 2 numbers
# @param x First number
# @param y Second number
# @return Sum of x and y
#
def addition(x,y):  
    return x+y


##
# @brief Function substract 2 numbers
# @param x First number
# @param y Second number
# @return Difference of x and y
#
def subtraction(x,y):
    return x-y

##
# @brief Function multiply 2 numbers
# @param x First number
# @param y Second number
# @return Product of x and y
#
def multiplication(x,y):
    return round(x*y,5)


##
# @brief Function divide 2 numbers
# @param x First number
# @param y Second number
# @return The share of x and y
#
def division(x,y):
    if y == 0:
        return "Error!"
    else:
        return round(x/y,5)


##
# @brief Function will do factorial of a number
# @param x Number of a factorial
# @return Factorial of x
#
def factorial(x):
    if x < 0:
        return "Error!"
    elif x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial(x-1)


##
# @brief Function aplifies a number
# @param x First number
# @param exponent Exponent of a number
# @return Aplified number
# 
def expon(x, exponent):
    if not isinstance(exponent, int) or exponent <0:
        return "Error!"
    elif x == 0:
        return 1
    else:
        return round(x ** exponent,5)

##
# @brief Function will do n-root of a number
# @param x Number under the root
# @param n Degree of a root
# @return n root of x
# 
def root(x,n):
    if x < 0:
        return "Error!"
    if n == 0:
        return "Error!"
    elif n == 1:
        return "Error!"
    else:
        return round (x ** (1/n),5)
    
##
# @brief Function will absolut value from number
# @param x Number 
# @return Absolut value of x
# 
def abs(x):
    if x >= 0:
        return x
    else:
        return x*(-1)
 

    