"""
    Fibonacci Using Recursion

    I/P: n: 1
    O/P: 1

    I/P: n: 20
    O/P: 6765
"""

class Solution:
    def fibonacci(self,n):
        if n<=1:
            return n

        return self.fibonacci(n-1)+self.fibonacci(n-2)