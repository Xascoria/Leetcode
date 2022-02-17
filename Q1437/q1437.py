from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_index = -1

        for i,j in enumerate(nums):
            if j == 1:
                if prev_index != -1:
                    d = i - prev_index - 1
                    if d < k:
                        return False
                prev_index = i
        return True