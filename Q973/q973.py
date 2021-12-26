from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        KeyFunc = lambda i: i[0]*i[0] + i[1]*i[1]
        points.sort(key=KeyFunc)
        return points[:k]