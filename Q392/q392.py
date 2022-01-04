class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        ptr = 0
        for i in t:
            if i==s[ptr]:
                ptr += 1
            if ptr == len(s):
                return True
        return False