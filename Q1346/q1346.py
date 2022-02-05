#1346
from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()
        for i in arr:
            if i*2 in d or (i%2==0 and i//2 in d):
                return True
            d.add(i)
        return False
        