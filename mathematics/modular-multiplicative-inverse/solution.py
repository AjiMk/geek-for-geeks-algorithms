class Solution:
    def modInverse(self,a,m):
        for x in range(1, m+1):
            if ((a%m) * (x%m))%m==1:
                return x
        return -1