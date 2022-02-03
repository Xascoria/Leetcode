from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1 = {}
        d2 = {}
        d3 = {}
        d4 = {}
        for i in nums1:
            d1[i] = d1.get(i, 0) + 1
        for i in nums2:
            d2[i] = d2.get(i, 0) + 1
        for i in nums3:
            d3[i] = d3.get(i, 0) + 1
        for i in nums4:
            d4[i] = d4.get(i, 0) + 1
            
        cd1 = {}
        for i in d1:
            for j in d2:
                cd1[i+j] = cd1.get(i+j,0) + d1[i] * d2[j]

        output = 0
        for i in d3:
            for j in d4:
                if 0-(i+j) in cd1:
                    output += cd1[0-(i+j)] * d3[i] * d4[j]
        return output



nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
x = Solution()
print( x.fourSumCount(nums1,nums2,nums3,nums4) )