##
# @file profiling.py
# 
# @brief Calculates the standard deviation 
# @author Aleš Recman

import sys, re, math_lib #, statistics

##
# @brief reads the nubmers from stdin, and prints their standard deviation
#
def profiling():
    nums:list[float] = readNumbers()
    print(standardDeviation(nums))
    # print(statistics.stdev(nums)) # sample result
    

##
# @brief reads numbers on stdin
# 
# @return list of numbers read from stdin
def readNumbers():
    inputString = sys.stdin.read().strip()
    numsString = re.split(r"\s+", inputString) #splits the numbers by white characters 
    nums = [float(num) for num in numsString] 
    return nums


##
# @brief sums the input numbers
#
# @param nums numbers for which the sum is calculated
#
# @return the sum of input numbers
def sum(nums):
    sum = 0
    for num in nums:
        sum = math_lib.addition(sum, num)

    return sum

##
# @brief calculates the x with strip in the standard deviation formula
#
# @param nums numbers for which the sWithStrip is calculated
#
# @return x with strip in the standard deviation formula
def calculateXWithStrip(nums):
    numSum = sum(nums)
    inverseN = math_lib.division(1, len(nums))
    return math_lib.multiplication(inverseN, numSum)

##
# @brief calculates the standard diviation based on the formula in the specification
#
# @param nums numbers for which the standard deviation is calculated
#
# @return the standard deviation for numbers provided
def standardDeviation(nums):
    # computing the parenthesis in the formula
    xWithStrip = calculateXWithStrip(nums)
    xWithStripSquared = math_lib.expon(xWithStrip, 2)

    numsSquared = [math_lib.expon(num, 2) for num in nums] 
    sumOfnumsSquared = sum(numsSquared)
    
    parenthesis = math_lib.subtraction(sumOfnumsSquared, math_lib.multiplication(xWithStripSquared,len(nums)))

    # multiplying the parenthesis by 1 over n - 1, where N is the number of elements
    oneOverNMinusOne = math_lib.division(1,math_lib.subtraction(len(nums), 1))

    numUnderSqrt = math_lib.multiplication(oneOverNMinusOne, parenthesis)

    # returning the square root
    return math_lib.root(numUnderSqrt,2)


if __name__ == "__main__":
    profiling()
