from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [0] * (len(nums)//2)
        negative = [0] * (len(nums)//2)
        pptr = nptr = 0

        for i in nums:
            if i > 0:
                positive[pptr] = i
                pptr += 1
            else:
                negative[nptr] = i
                nptr += 1
        
        output = [0] * len(nums)
        output[::2] = positive
        output[1::2] = negative
        return output

## Faster
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for i in nums:
            if i > 0:
                positive.append(i)
            else:
                negative.append(i)
        
        output = nums
        output[::2] = positive
        output[1::2] = negative
        return output
