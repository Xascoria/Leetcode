

class Solution:
    def arrangeCoins(self, m: int) -> int:
        r1 = (-1 + (1 + 8 * m)**0.5) / 2
        #r2 = (-1 - (1 + 8 * m)**0.5) / 2
        return int(r1)