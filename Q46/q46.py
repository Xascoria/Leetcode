from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursion(cur_list, cur_remains):
            if len(cur_remains) == 0:
                return [cur_list]
            output = []
            for i, j in enumerate(cur_remains):
                output += recursion( cur_list+[j], cur_remains[:i]+cur_remains[i+1:] )
            return output
        return recursion([], nums)

x = Solution()
print( x.permute([1,2,3]) )
