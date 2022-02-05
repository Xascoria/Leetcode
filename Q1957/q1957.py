
#1957
class Solution:
    def makeFancyString(self, s: str) -> str:
        out = ""
        start = s[0]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                start += s[i]
            else:
                out += start[:2]
                start = s[i]
        out += start[:2]
        return out

x = Solution()
print( x.makeFancyString('leeetcode') )