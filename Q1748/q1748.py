
from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a = 0
        for i in set(nums):
            if nums.count(i) == 1:
                a += i
        return a