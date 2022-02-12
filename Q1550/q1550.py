from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cur_count = 0
        for i in arr:
            if i%2 == 0:
                cur_count = 0
            else:
                cur_count += 1
                if cur_count == 3:
                    return True
        return False
                    