from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recursion(cur_start, layer):
            if layer == 0:
                return [[i] for i in range(cur_start, n+1)]
            return sum([[[i]+j for j in recursion(i+1, layer-1)] for i in range(cur_start, n+1)],[])
        return recursion(1, k-1)
                
x = Solution()
print( x.combine(7,2) )