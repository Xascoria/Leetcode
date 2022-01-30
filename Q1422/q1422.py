class Solution:
    def maxScore(self, s: str) -> int:
        out = 0
        for i in range(1, len(s)):
            out = max(out, s[:i].count("0")+s[i:].count("1"))
        return out
            

x = Solution()
print( x.maxScore("011101") )