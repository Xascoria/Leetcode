from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0: return

        ptr1 = m-1
        ptr2 = len(nums2)-1
        for i in range(len(nums1)-1, -1, -1):
            if (nums1[ptr1] < nums2[ptr2] and ptr2 >= 0) or ptr1 == -1:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
        
x = Solution()
print( x.merge([2,0],1,[1],1) )