"""
    Power of a number using recursion

    I/P: n: 2 p: 4
    O/P: 16

    I/P: n: 9 p: 9
    O/P: 387420489
"""

class Solution:
    def RecursivePower(self,n,p):
        if p<1:
            return 1
        return n*self.RecursivePower(n, p-1)
