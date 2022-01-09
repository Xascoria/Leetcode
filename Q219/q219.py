from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set = set()
        for i in range(min(len(nums), k+1)):
            if nums[i] in window_set:
                return True
            window_set.add(nums[i])
        
        for i in range(k+1, len(nums)):
            window_set.remove( nums[i-k-1] )
            if nums[i] in window_set:
                return True
            window_set.add(nums[i])
        return False