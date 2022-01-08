from typing import List

from fractions import Fraction
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1

        line_dict = {}
        first_occur_dict = {}

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                yc = points[j][1] - points[i][1]
                xc = points[j][0] - points[i][0]
                if xc == 0:
                    line_info = (float("inf"), points[j][0])
                elif yc == 0:
                    line_info = (0, points[j][1])
                else:
                    c = points[j][1] - Fraction(yc,xc) * points[j][0]
                    line_info = (Fraction(yc,xc), c)
                if line_info not in first_occur_dict:
                    first_occur_dict[line_info] = i
                    line_dict[line_info] = 2
                elif first_occur_dict[line_info] == i:
                    line_dict[line_info] += 1
            
        return max(line_dict.values())
                