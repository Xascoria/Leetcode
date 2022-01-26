class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        start = nums[0]
        start_index = -1
        for i in range(1, len(nums)):
            if nums[i] != start:
                start_index = i
                break
        if start_index == -1:
            return 0
        end = nums[-1]
        end_index = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] != end:
                end_index = i
                break
        return max(0, end_index - start_index + 1)