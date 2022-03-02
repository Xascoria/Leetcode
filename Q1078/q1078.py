from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s = text.split()
        output = []
        for i in range(len(s)-2):
            if s[i] == first and s[i+1] == second:
                output.append(s[i+2])
        return output

x = Solution()
print( x.findOcurrences("we will we will rock you", "we", "will") )