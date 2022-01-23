class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        output = 0
        for i in range(0, len(s)-2):
            output += len(set(s[i:i+3])) == 3
        return output

x = Solution()
print( x.countGoodSubstrings("abcdef") )