class Solution:
    def termOfGP(self,A,B,N):
        R = B/A
        return A*R**(N-1)