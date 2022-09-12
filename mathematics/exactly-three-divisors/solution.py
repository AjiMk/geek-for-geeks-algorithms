import math

class Solution:
    def exactly3Divisors(self,N):
        count = 0
        for i in range(2, math.floor(N**0.5)+1):
            if self.isPrime(i):
                count+=1
        return count

    def isPrime(self, N):
        if N==1:
            return False
        if N==2 or N==3:
            return True

        for i in range(2, math.floor(N**0.5)+1):
            if N%i==0:
                return False
        return True
