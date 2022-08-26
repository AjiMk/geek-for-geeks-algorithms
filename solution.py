class Solution:
    def multiplicationUnderModulo(self,a,b):
        mod = 10**9+7
        return (a%mod*b%mod)%mod
