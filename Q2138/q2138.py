from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s = s.ljust( (0--len(s)//k)*k, fill )
        return [s[i:i+k]for i in range(0,len(s),k)]

x = Solution()
print( x.divideString("abcdecasc", 6, "z") )