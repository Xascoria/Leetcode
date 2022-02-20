class Solution:
    def minSteps(self, n: int) -> int:
        output = 0
        for i in range(2,n+1):
            while n%i==0:
                output += i
                n//=i
        return output