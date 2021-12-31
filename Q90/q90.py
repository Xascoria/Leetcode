from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def recursion(current_set, current_index):
            if current_index == len(nums):
                return [current_set]

            return recursion(current_set + [nums[current_index]],current_index+1) + recursion(current_set,current_index+1)
        res = recursion([],0)
        return set(map(tuple,res))

        