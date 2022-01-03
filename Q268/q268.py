class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        org = 0
        for i in range(len(nums)+1):
            org ^= i
        for i in nums:
            org ^= i
        return org