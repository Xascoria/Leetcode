import math

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        output = 1
        for i in range(n):
            output += 9 * math.prod(range(10-i,10))
        return output