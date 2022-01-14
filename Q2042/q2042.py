class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [*map(int,(i for i in s.split() if i.isdigit()))]
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                return False
        return True