
import sys, re


##
# @brief the main fucion 
#
def profiling():
    numbers:list[int] = readNumbers()
    numbers.count()
    

##
# @brief reads numbers on stdin
# 
# @return list of numbers read from stdin
def readNumbers():
    inputString = sys.stdin.read().strip()
    numbers = re.split(r"\s+", inputString)
    print(numbers)










if __name__ == "__main__":
    profiling()
