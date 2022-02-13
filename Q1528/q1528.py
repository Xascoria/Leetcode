from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [' ']*len(s)
        for i,j in enumerate(indices):
            arr[j] = s[i]
        return ''.join(arr)