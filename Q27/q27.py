class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = 0
        if len(nums) == 0: return 0
        
        while nums[-1-removed] == val:
            removed += 1
            if removed == len(nums):
                return len(nums)-removed

        index = 0
        while index < len(nums) - removed:
            if nums[index] == val:
                nums[index], nums[-1-removed] = nums[-1-removed], nums[index]
                removed += 1
            while nums[-1-removed] == val:
                removed += 1
            index += 1
        return len(nums)-removed
