from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = nums[::2]
        odd = nums[1::2]
        even.sort()
        odd.sort(reverse=1)

        output = []
        for i,j in zip(even,odd):
            output += [i,j]
        if len(even) == len(odd):
            return output
        return output + [even[-1]]