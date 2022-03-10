from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums.sort(key=lambda x:int( ''.join(str(mapping[int(j)])for j in str(x)) ))
        return nums

x = Solution()
print( x.sortJumbled([8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]) )