from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        delete_from_left = max(min_index, max_index)+1
        delete_from_right = max(len(nums)-min_index, len(nums)-max_index)

        a,b= min(min_index, max_index), max(min_index,max_index)
        delete_from_both = a+1 + len(nums)-b
        return min(delete_from_left, delete_from_right, delete_from_both)