from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a = num//3
        if a*3 == num:
            return [a-1,a,a+1]
        return []