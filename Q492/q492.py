from typing import List
import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a = math.isqrt(area)
        while not (area/a).is_integer():
            a -= 1
        print(a,area//a)
        return [area//a,a]

