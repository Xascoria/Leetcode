from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        s = [1]
        for i in range(n-1):
            s = s + [i+2] + s
        start = [0] * n
        output = [0]
        for ind in s:
            start[-ind] = (1,0)[start[-ind]]
            output.append( int(''.join(map(str,start)),2) )
        return output

x = Solution()
print( x.grayCode(2) )