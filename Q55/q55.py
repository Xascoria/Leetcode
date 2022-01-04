from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reached = [True] + [False] * (len(nums)-1)
        for i in range(len(can_reached)):
            if not can_reached[i]:
                return False
            for j in range(nums[i]+i, i, -1):
                if j >= len(can_reached)-1:
                    return True
                if can_reached[j]:
                    break
                can_reached[j] = True
        return True

x = Solution()
print( x.canJump([2,3,1,1,4]) )
print( x.canJump([0]) )