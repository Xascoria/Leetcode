class Solution:
    def reverse(self, x: int) -> int:
        sign = x < 0
        res = int(str(abs(x))[::-1]) * [1,-1][sign]
        if not (-(2**31) <= res <= ((2**31)-1)):
            return 0
        return res
        