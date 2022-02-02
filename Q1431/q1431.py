from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mc = max(candies)
        return [i+extraCandies >= mc for i in candies]