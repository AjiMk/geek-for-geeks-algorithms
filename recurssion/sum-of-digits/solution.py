"""
    Sum of digits using recurssion

    I/P: n: 253
    O/P: 10

    I/P: n: 9987
    O/P: 33
"""

import math
def sumOfDigits(n):
    if n<=0:
        return 0
    return n%10+sumOfDigits( math.floor( n/10 ) )

inputs = [
    253,   # 10
    9987,  # 33
    10021, ## 4
    23201  ## 8
]

for number in inputs:
    print( sumOfDigits(number) )