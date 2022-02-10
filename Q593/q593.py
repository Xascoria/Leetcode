from typing import List
import math


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if len(set([tuple(p1),tuple(p2),tuple(p3),tuple(p4)])) != 4:
            return False

        p1darr = [ math.dist(p1, p2), math.dist(p1, p3), math.dist(p1, p4) ]
        if len(set(p1darr)) != 2:
            return False
        a,b = min(p1darr), max(p1darr)
        if p1darr.count(a) != 2 or p1darr.count(b) != 1:
            return False
        max_ind = p1darr.index(b)

        if max_ind == 0:
            c,d = math.dist(p2, p3), math.dist(p2, p4)
        elif max_ind == 1:
            c,d = math.dist(p2, p3), math.dist(p3, p4)
        else:
            c,d = math.dist(p2, p4), math.dist(p3, p4)

        if c != d or c != a:
            return False
        if round(2 * a * a,6) !=  round(b * b,6):
            return False
        return True

x = Solution()
print( x.validSquare( p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]) )