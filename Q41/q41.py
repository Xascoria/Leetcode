class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        checklist = [False] * (len(nums)+1)
        for i in nums:
            if (i-1) < len(nums) and i>0:
                checklist[i-1] = True
        
        return checklist.index(False)+1