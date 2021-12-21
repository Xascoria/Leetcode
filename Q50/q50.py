class Solution:
    def myPow(self, x: float, n: int) -> float:
        n_negative = n < 0
        
        out = 1
        x_10000 = 1
        for _ in range(10000):
            x_10000 *= x
            
        i=0
        while i < abs(n):
            if i < abs(n)-10000:
                out *= x_10000
                i += 10000
                continue
            out *= x
            i += 1
        
        if n_negative:
            out = 1/out
        return out