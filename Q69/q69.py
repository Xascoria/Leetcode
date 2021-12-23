class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0, 65536, 100):
            if i*i > x:
                break
        for j in range(i-100, i+1):
            if j*j < x:
                pass
            elif j*j == x:
                return j
            else:
                return j-1

x = Solution()
print( x.mySqrt(2088437940) )