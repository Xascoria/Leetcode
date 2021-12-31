from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recursion(current_set, cur_index):
            if cur_index == len(nums):
                return [current_set]

            return recursion(current_set,cur_index+1) + recursion(current_set+[nums[cur_index]], cur_index+1)
        return recursion([],0)

