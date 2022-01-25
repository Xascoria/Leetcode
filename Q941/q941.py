from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        reached_peak = False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if arr[i] < arr[i+1]:
                if reached_peak:
                    return False
            else:
                if i == 0:
                    return False
                reached_peak = True
                
        return reached_peak