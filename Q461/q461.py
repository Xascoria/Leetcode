

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x^y
        out = 0
        while z:
            out += z%2
            z//=2
        return out

x = Solution()
print( x.hammingDistance(1,4) )