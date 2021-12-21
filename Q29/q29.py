class Solution:
    def clamp(self,num):
        return min((2**31)-1, max(-(2**31), num))
    
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        is_negative = (dividend < 0) + (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        d10 = 0
        for i in range(100):
            d10 += divisor
        
        while dividend >= divisor:
            if dividend >= d10:
                dividend -= d10
                res += 100
                continue
            dividend -= divisor
            res += 1
        return self.clamp(res * [1,-1,1][is_negative])