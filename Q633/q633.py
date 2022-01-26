import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0: return True
        p = math.ceil(c**0.5) + (c**0.5).is_integer()
        for i in range(1, p):
            #print(c - i*i)
            if ((c-i*i)**0.5).is_integer():
                return True
        return False

x = Solution()
print( x.judgeSquareSum(3) )