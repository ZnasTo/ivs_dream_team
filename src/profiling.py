
import sys, re, math_lib

##
# @brief the main fucion 
#
def profiling():
    nums:list[float] = readNumbers()
    standardDeviation(nums)
    
    
    
    

    

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
# @return the sum of input numbers
def sum(nums):
    sum = 0
    for num in nums:
        sum = math_lib.addition(sum, num)

    return sum


##
# @brief computes the x with strip in the standard deviation formula
#
# @return x with strip in the standard deviation formula
def computeXWithStrip(nums):
    numSum = sum(nums)
    inverseN = math_lib.division(1, len(nums))
    return math_lib.multiplication(inverseN, numSum)



def standardDeviation(numbs):
    # computing the second part of the formula
    xWithStrip = computeXWithStrip(numbs)
    xWithStripSquared = math_lib.expon(xWithStrip, 2)

    numsSquared = [math_lib.expon(num, 2) for num in numbs] 
    sumOfnumsSquared = sum(numsSquared)
    print(numsSquared)

if __name__ == "__main__":
    profiling()
