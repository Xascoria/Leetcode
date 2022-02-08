from re import I
from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        d = {}
        stack = [id]
        for i in employees:
            eid, im, sub = i.id, i.importance, i.subordinates
            d[eid] = (im, sub)
        output = 0
        while stack:
            cur = d[stack.pop()]
            output += cur[0]
            stack += cur[1]
        return output

x = Solution()
print( x.getImportance([[1,2,[5]],[5,-3,[]]], id = 5) )