from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        aux_arr = [0] + [float("inf")]*(len(nums)-1)

        for i in range(len(nums)-1):
            for j in range(i+1,i+1+nums[i]):
                aux_arr[j] = min(aux_arr[i] + 1, aux_arr[j])
                if j == len(nums)-1:
                    return aux_arr[j]
        return 0

