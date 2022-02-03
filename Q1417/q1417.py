class Solution:
    def reformat(self, s: str) -> str:
        alpha = []
        nums = []
        for i in s:
            if i.isdigit():
                nums.append(i)
            else:
                alpha.append(i)
        if abs(len(alpha) - len(nums)) > 1:
            return ""

        s = ''.join(i+j for i,j in zip(alpha, nums))
        if len(alpha) > len(nums):
            s += alpha[-1]
        if len(alpha) < len(nums):
            s = nums[-1] + s
        return s
