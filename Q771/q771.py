class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        out = 0
        for i in jewels:
            out += stones.count(i)
        return out