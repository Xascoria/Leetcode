
class Solution:
    def checkString(self, s: str) -> bool:
        if "a" not in s or "b" not in s:
            return True
        b_index = s.index("b")
        a_index = len(s) - 1 - s[::-1].index("a")
        return b_index > a_index

x = Solution()
print( x.checkString("abab") )